#!/usr/bin/env python3
import csv
import glob
import json
import logging
import os
import time
import uuid
from typing import Any, Dict, List, Optional, get_args
from collections import defaultdict

import torch
import wandb
import numpy as np
import evaluate
from datasets import load_dataset, Dataset
from openai.types.fine_tuning.dpo_hyperparameters import DpoHyperparameters
from openai.types.fine_tuning.dpo_method import DpoMethod
from openai.types.fine_tuning.fine_tuning_job import (
    FineTuningJob,
    Hyperparameters,
    Method,
)
from openai.types.fine_tuning.supervised_hyperparameters import (
    SupervisedHyperparameters,
)
from openai.types.fine_tuning.supervised_method import SupervisedMethod
from peft import LoraConfig, TaskType, get_peft_model, prepare_model_for_kbit_training
from torch.nn.utils.rnn import pad_sequence
from transformers import (
    AutoModelForImageTextToText,
    AutoProcessor,
    BitsAndBytesConfig,
    Trainer,
    TrainingArguments,
    EvalPrediction,
    DataCollatorForLanguageModeling,
)
from trl import DPOConfig, DPOTrainer

# Extract method type values from OpenAI API type definition
METHOD_TYPES = get_args(Method.model_fields["type"].annotation)
METHOD_TYPE_SUPERVISED, METHOD_TYPE_DPO, METHOD_TYPE_REINFORCEMENT = METHOD_TYPES

# Constants
MODEL_ID = "HuggingFaceTB/SmolVLM2-256M-Video-Instruct"
OUTPUT_BASE_DIR = "data/models"
FILES_DIR = "data/files"
SMOLVLM_TARGET_MODULES = [
    "down_proj",
    "gate_proj",
    "k_proj",
    "o_proj",
    "q_proj",
    "up_proj",
    "v_proj",
]
MEMORY_CONVERSION_FACTOR = 1024**3

# PEFT method constants
PEFT_METHOD_NONE = "none"
PEFT_METHOD_LORA = "lora"
PEFT_METHOD_QLORA = "qlora"

# Enhanced monitoring configuration
MONITORING_CONFIG = {
    'patience': 50,  # Steps to wait for improvement
    'min_improvement': 0.001,  # Minimum loss improvement
    'max_loss_threshold': 10.0,  # Fail if loss exceeds this
    'log_frequency': 1,  # Detailed logging every N steps
    'grad_norm_threshold': 50.0,  # Warn if gradient norm exceeds this
    'enable_wandb': True,  # Enable Weights & Biases logging
    'enable_generation_metrics': True,  # Enable BLEU/METEOR/ROUGE
}

class VisionLanguagePerformanceMonitor:
    """Enhanced performance monitor for vision-language models"""
   
    def __init__(self, patience: int = 50, min_improvement: float = 0.001,
                 max_loss_threshold: float = 10.0):
        self.patience = patience
        self.min_improvement = min_improvement
        self.max_loss_threshold = max_loss_threshold
        self.best_loss = float('inf')
        self.wait_count = 0
        self.step_count = 0
        self.loss_history = []
       
    def should_stop(self, current_loss: float) -> bool:
        self.step_count += 1
        self.loss_history.append(current_loss)
       
        # Fail fast if loss explodes
        if current_loss > self.max_loss_threshold:
            raise RuntimeError(f"Training failed: Loss exploded to {current_loss:.4f} at step {self.step_count}")
       
        # Check for NaN/Inf
        if not np.isfinite(current_loss):
            raise RuntimeError(f"Training failed: Loss is {current_loss} at step {self.step_count}")
       
        # Check for improvement
        if current_loss < self.best_loss - self.min_improvement:
            self.best_loss = current_loss
            self.wait_count = 0
            return False
        else:
            self.wait_count += 1
            if self.wait_count >= self.patience:
                logging.warning(f"No improvement for {self.patience} steps. Best loss: {self.best_loss:.4f}")
       
        return False

class UniversalTokenAnalyzer:
    """Universal token analyzer that handles both vision and text-only datasets"""
   
    def __init__(self, processor):
        self.processor = processor
        self.tokenizer = processor.tokenizer if hasattr(processor, 'tokenizer') else None
       
        # Special tokens - handle potential missing tokens gracefully
        self.pad_token_id = getattr(self.tokenizer, 'pad_token_id', None) if self.tokenizer else None
        self.bos_token_id = getattr(self.tokenizer, 'bos_token_id', None) if self.tokenizer else None
        self.eos_token_id = getattr(self.tokenizer, 'eos_token_id', None) if self.tokenizer else None
       
        # Vision tokens - handle gracefully if not present
        self.image_token_id = None
        self.video_token_id = None
       
        # Try to find vision tokens
        if self.tokenizer and hasattr(self.tokenizer, 'additional_special_tokens') and self.tokenizer.additional_special_tokens:
            try:
                if "<image>" in self.tokenizer.additional_special_tokens:
                    self.image_token_id = self.tokenizer.additional_special_tokens_ids[
                        self.tokenizer.additional_special_tokens.index("<image>")
                    ]
                if "<video>" in self.tokenizer.additional_special_tokens:
                    self.video_token_id = self.tokenizer.additional_special_tokens_ids[
                        self.tokenizer.additional_special_tokens.index("<video>")
                    ]
            except (ValueError, AttributeError, IndexError):
                pass  # Vision tokens not available
   
    def analyze_batch(self, batch: Dict[str, torch.Tensor]) -> Dict[str, Any]:
        """Universal batch analysis that works for any dataset type"""
        analysis = {}
       
        # Analyze text components (always present)
        if 'input_ids' in batch:
            analysis.update(self._analyze_input_ids(batch['input_ids']))
           
        if 'labels' in batch:
            analysis.update(self._analyze_labels(batch['labels'], batch.get('input_ids')))
           
        if 'attention_mask' in batch:
            analysis.update(self._analyze_attention_mask(batch['attention_mask']))
           
        # Analyze vision components (if present)
        if 'pixel_values' in batch:
            analysis.update(self._analyze_pixel_values(batch['pixel_values']))
        else:
            # Mark as text-only
            analysis['vision_'] = {
                'type': 'text_only',
                'has_vision_data': False
            }
           
        return analysis
   
    def _analyze_input_ids(self, input_ids: torch.Tensor) -> Dict[str, Any]:
        """Analyze input_ids with universal compatibility"""
        analysis = {'text_': {}}
       
        batch_size, seq_len = input_ids.shape
        analysis['text_']['batch_size'] = batch_size
        analysis['text_']['seq_length'] = seq_len
        analysis['text_']['vocab_coverage'] = len(torch.unique(input_ids))
       
        # Special token counts (handle missing tokens gracefully)
        if self.pad_token_id is not None:
            pad_count = (input_ids == self.pad_token_id).sum().item()
            analysis['text_']['pad_token_count'] = pad_count
            analysis['text_']['pad_ratio'] = pad_count / (batch_size * seq_len)
           
        if self.image_token_id is not None:
            img_count = (input_ids == self.image_token_id).sum().item()
            analysis['text_']['image_token_count'] = img_count
           
        if self.video_token_id is not None:
            vid_count = (input_ids == self.video_token_id).sum().item()
            analysis['text_']['video_token_count'] = vid_count
           
        # Sequence length distribution
        if self.pad_token_id is not None:
            seq_lengths = []
            for seq in input_ids:
                actual_length = (seq != self.pad_token_id).sum().item()
                seq_lengths.append(actual_length)
           
            analysis['text_']['seq_lengths'] = {
                'mean': np.mean(seq_lengths),
                'std': np.std(seq_lengths),
                'min': min(seq_lengths),
                'max': max(seq_lengths)
            }
           
        return analysis
   
    def _analyze_labels(self, labels: torch.Tensor, input_ids: Optional[torch.Tensor] = None) -> Dict[str, Any]:
        """Analyze labels with proper masking validation"""
        analysis = {'labels_': {}}
       
        # Basic stats
        valid_mask = labels != -100
        total_tokens = labels.numel()
        valid_tokens = valid_mask.sum().item()
       
        analysis['labels_']['total_tokens'] = total_tokens
        analysis['labels_']['valid_tokens'] = valid_tokens
        analysis['labels_']['valid_ratio'] = valid_tokens / total_tokens if total_tokens > 0 else 0
       
        # Check vision token masking
        if self.image_token_id is not None:
            image_tokens_in_labels = (labels == self.image_token_id).sum().item()
            analysis['labels_']['image_tokens_in_labels'] = image_tokens_in_labels
           
        if self.video_token_id is not None:
            video_tokens_in_labels = (labels == self.video_token_id).sum().item()
            analysis['labels_']['video_tokens_in_labels'] = video_tokens_in_labels
       
        # Per-sequence analysis
        valid_per_seq = valid_mask.sum(dim=1).cpu().numpy()
        analysis['labels_']['valid_per_seq'] = {
            'mean': float(np.mean(valid_per_seq)),
            'std': float(np.std(valid_per_seq)),
            'min': int(np.min(valid_per_seq)),
            'max': int(np.max(valid_per_seq))
        }
       
        return analysis
   
    def _analyze_attention_mask(self, attention_mask: torch.Tensor) -> Dict[str, Any]:
        """Analyze attention mask"""
        analysis = {'attention_': {}}
       
        total_positions = attention_mask.numel()
        attended_positions = attention_mask.sum().item()
       
        analysis['attention_']['total_positions'] = total_positions
        analysis['attention_']['attended_positions'] = attended_positions
        analysis['attention_']['attention_ratio'] = attended_positions / total_positions
       
        # Per-sequence attention lengths
        attention_lengths = attention_mask.sum(dim=1).cpu().numpy()
        analysis['attention_']['lengths'] = {
            'mean': float(np.mean(attention_lengths)),
            'std': float(np.std(attention_lengths)),
            'min': int(np.min(attention_lengths)),
            'max': int(np.max(attention_lengths))
        }
       
        return analysis
   
    def _analyze_pixel_values(self, pixel_values: torch.Tensor) -> Dict[str, Any]:
        """Analyze pixel values (images/videos) - handles None gracefully"""
        analysis = {'vision_': {}}
       
        if pixel_values is None:
            analysis['vision_']['type'] = 'text_only'
            analysis['vision_']['has_vision_data'] = False
            return analysis
       
        # Shape analysis
        shape = list(pixel_values.shape)
        analysis['vision_']['shape'] = shape
        analysis['vision_']['batch_size'] = shape[0]
        analysis['vision_']['has_vision_data'] = True
       
        if len(shape) == 5:  # Video: [batch, frames, channels, height, width]
            analysis['vision_']['frames'] = shape[1]
            analysis['vision_']['channels'] = shape[2]
            analysis['vision_']['height'] = shape[3]
            analysis['vision_']['width'] = shape[4]
            analysis['vision_']['type'] = 'video'
        elif len(shape) == 4:  # Image: [batch, channels, height, width]
            analysis['vision_']['channels'] = shape[1]
            analysis['vision_']['height'] = shape[2]
            analysis['vision_']['width'] = shape[3]
            analysis['vision_']['type'] = 'image'
        else:
            analysis['vision_']['type'] = 'unknown_vision_format'
           
        # Pixel statistics
        analysis['vision_']['pixel_stats'] = {
            'mean': float(pixel_values.mean().item()),
            'std': float(pixel_values.std().item()),
            'min': float(pixel_values.min().item()),
            'max': float(pixel_values.max().item())
        }
       
        # Check for zero/empty frames
        if len(shape) == 5:
            zero_frames = 0
            for b in range(shape[0]):
                for f in range(shape[1]):
                    if pixel_values[b, f].sum().item() == 0:
                        zero_frames += 1
            analysis['vision_']['zero_frames'] = zero_frames
           
        return analysis

class MemoryTracker:
    """Track GPU memory usage during training"""
   
    def __init__(self):
        self.memory_log = defaultdict(list)
        self.peak_memory = 0
       
    def track_memory(self, phase: str):
        """Track memory usage at different phases"""
        if torch.cuda.is_available():
            current_memory = torch.cuda.memory_allocated() / 1024**3  # GB
            max_memory = torch.cuda.max_memory_allocated() / 1024**3  # GB
           
            self.memory_log[phase].append(current_memory)
            self.peak_memory = max(self.peak_memory, max_memory)
           
    def get_memory_summary(self) -> Dict[str, float]:
        """Get memory usage summary"""
        summary = {}
        for phase, memories in self.memory_log.items():
            if memories:
                summary[f"memory_{phase}_avg"] = np.mean(memories)
                summary[f"memory_{phase}_max"] = np.max(memories)
        summary["memory_peak_overall"] = self.peak_memory
        return summary

class EnhancedUniversalTrainer(Trainer):
    """Enhanced trainer that works universally with any dataset type and provides comprehensive monitoring"""
   
    def __init__(self, *args, monitoring_config=None, enable_generation_metrics=True,
                 dataset_type="auto", **kwargs):
        super().__init__(*args, **kwargs)
       
        # Initialize monitoring components
        config = monitoring_config or MONITORING_CONFIG
        self.performance_monitor = VisionLanguagePerformanceMonitor(
            patience=config['patience'],
            min_improvement=config['min_improvement'],
            max_loss_threshold=config['max_loss_threshold']
        )
       
        self.token_analyzer = UniversalTokenAnalyzer(self.tokenizer if hasattr(self, 'tokenizer') else None)
        self.log_frequency = config['log_frequency']
        self.grad_norm_threshold = config['grad_norm_threshold']
        self.dataset_type = dataset_type
       
        # Metrics tracking
        self.metrics_history = defaultdict(list)
        self.anomaly_count = 0
       
        # Generation metrics setup
        self.enable_generation_metrics = enable_generation_metrics and config['enable_generation_metrics']
        if self.enable_generation_metrics:
            try:
                self.generation_metrics = evaluate.combine(["bleu", "meteor", "rouge"])
                self.metrics_tracker = {}
                logging.info("✅ Generation metrics (BLEU, METEOR, ROUGE) initialized")
            except Exception as e:
                logging.warning(f"Failed to initialize generation metrics: {e}")
                self.enable_generation_metrics = False
       
        # Memory tracking
        self.memory_tracker = MemoryTracker()
       
        # WandB configuration
        self.enable_wandb = config.get('enable_wandb', False)
       
    def compute_metrics(self, eval_pred: EvalPrediction) -> Dict:
        """Enhanced compute metrics with generation quality evaluation"""
        if not self.enable_generation_metrics:
            return {}
           
        try:
            all_labels = eval_pred.label_ids
            all_preds = eval_pred.predictions
           
            # Handle -100 labels
            all_labels[all_labels == -100] = self.tokenizer.pad_token_id
           
            # Decode predictions and references
            references = self.tokenizer.batch_decode(all_labels, skip_special_tokens=True)
            predictions = self.tokenizer.batch_decode(all_preds, skip_special_tokens=True)
           
            # Clean up empty or whitespace-only strings
            cleaned_refs = []
            cleaned_preds = []
            for ref, pred in zip(references, predictions):
                ref_clean = ref.strip()
                pred_clean = pred.strip()
                if ref_clean and pred_clean:
                    cleaned_refs.append(ref_clean)
                    cleaned_preds.append(pred_clean)
           
            if not cleaned_refs:
                logging.warning("No valid prediction-reference pairs found for metrics")
                return {}
           
            # Compute metrics
            eval_batch_metrics = self.generation_metrics.compute(
                predictions=cleaned_preds,
                references=cleaned_refs,
            )
           
            # Process metrics
            computed_metrics = {}
            for key, value in eval_batch_metrics.items():
                if isinstance(value, (list, np.ndarray)):
                    value = np.mean(value)
               
                # Update running average
                self.metrics_tracker[key] = np.mean([
                    self.metrics_tracker.get(key, 0.0),
                    value
                ])
                computed_metrics[f"eval_{key}"] = self.metrics_tracker[key]
           
            return computed_metrics
           
        except Exception as e:
            logging.warning(f"Failed to compute generation metrics: {e}")
            return {}
   
    def preprocess_logits_for_metrics(self, logits: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
        """Memory optimization: return only predicted token IDs"""
        pred_ids = torch.argmax(logits, dim=-1)
        return pred_ids
       
    def compute_loss(self, model, inputs, return_outputs=False, **kwargs):
        """Enhanced compute_loss with universal monitoring"""
       
        # Track memory before forward pass
        self.memory_tracker.track_memory("before_forward")
       
        # Log input details periodically
        if self.state.global_step % self.log_frequency == 0:
            self._log_batch_details(inputs)
       
        # Compute loss normally
        if self.label_smoother is not None and "labels" in inputs:
            labels = inputs.pop("labels")
        else:
            labels = None
           
        outputs = model(**inputs)
       
        # Track memory after forward pass
        self.memory_tracker.track_memory("after_forward")
       
        if self.args.past_index >= 0:
            self._past = outputs[self.args.past_index]

        if labels is not None:
            if hasattr(outputs, "loss"):
                loss = outputs.loss
            else:
                loss = self.label_smoother(outputs, labels, shift_labels=True)
        else:
            if isinstance(outputs, dict) and "loss" not in outputs:
                raise ValueError(
                    "The model did not return a loss from the inputs, only the following keys: "
                    f"{','.join(outputs.keys())}. For reference, the inputs it received are {','.join(inputs.keys())}."
                )
            loss = outputs["loss"] if isinstance(outputs, dict) else outputs[0]

        # Monitor performance
        if loss is not None:
            loss_item = loss.item()
            self._monitor_training_step(loss_item, model)
       
        # Track memory after backward pass
        self.memory_tracker.track_memory("after_backward")
           
        return (loss, outputs) if return_outputs else loss
   
    def _log_batch_details(self, batch):
        """Log detailed batch information with universal support"""
        try:
            analysis = self.token_analyzer.analyze_batch(batch)
           
            # Flatten and log
            flat_metrics = self._flatten_dict(analysis)
           
            # Determine dataset type for cleaner logging
            dataset_type = "TEXT-ONLY"
            if 'vision_' in analysis and analysis['vision_'].get('has_vision_data', False):
                dataset_type = analysis['vision_'].get('type', 'VISION').upper()
           
            # Log to console with clear formatting
            print(f"\n{'='*80}")
            print(f"📊 STEP {self.state.global_step} BATCH ANALYSIS ({dataset_type})")
            print(f"{'='*80}")
           
            # Organize logging by category
            text_metrics = {k: v for k, v in flat_metrics.items() if k.startswith('text_')}
            label_metrics = {k: v for k, v in flat_metrics.items() if k.startswith('labels_')}
            attention_metrics = {k: v for k, v in flat_metrics.items() if k.startswith('attention_')}
            vision_metrics = {k: v for k, v in flat_metrics.items() if k.startswith('vision_')}
           
            if text_metrics:
                print("🔤 TEXT METRICS:")
                for k, v in text_metrics.items():
                    print(f"  {k}: {v}")
           
            if label_metrics:
                print("🏷️  LABEL METRICS:")
                for k, v in label_metrics.items():
                    print(f"  {k}: {v}")
           
            if attention_metrics:
                print("👁️  ATTENTION METRICS:")
                for k, v in attention_metrics.items():
                    print(f"  {k}: {v}")
           
            if vision_metrics:
                print("🖼️  VISION METRICS:")
                for k, v in vision_metrics.items():
                    print(f"  {k}: {v}")
           
            print(f"{'='*80}")
           
            # Log to wandb if enabled
            if self.enable_wandb and wandb.run is not None:
                wandb_metrics = {f"batch_analysis/{k}": v for k, v in flat_metrics.items()}
                wandb_metrics["batch_analysis/dataset_type"] = dataset_type
                wandb.log(wandb_metrics, step=self.state.global_step)
               
        except Exception as e:
            logging.warning(f"Failed to analyze batch at step {self.state.global_step}: {e}")
   
    def _monitor_training_step(self, loss: float, model):
        """Monitor training step for anomalies"""
        step = self.state.global_step
       
        # Get gradient norm
        grad_norm = self._get_grad_norm(model)
       
        # Performance monitoring
        try:
            self.performance_monitor.should_stop(loss)
        except RuntimeError as e:
            logging.error(f"Training stopped due to performance issue: {e}")
            raise e
       
        # Enhanced console logging
        metrics = {
            'train/loss': loss,
            'train/learning_rate': self.optimizer.param_groups[0]['lr'] if hasattr(self, 'optimizer') and self.optimizer else 0.0,
            'train/step': step,
        }
       
        if grad_norm is not None:
            metrics['train/grad_norm'] = grad_norm
           
        # Check for anomalies
        anomalies = self._check_anomalies(loss, grad_norm, step)
        if anomalies:
            metrics['train/anomaly_count'] = len(anomalies)
            self.anomaly_count += len(anomalies)
       
        # Enhanced console logging
        current_lr = self.optimizer.param_groups[0]['lr'] if hasattr(self, 'optimizer') and self.optimizer else 0.0
        print(f"\n📈 STEP {step} METRICS:")
        print(f"  Loss: {loss:.6f} | LR: {current_lr:.2e}", end="")
        if grad_norm is not None:
            print(f" | Grad Norm: {grad_norm:.4f}", end="")
        if anomalies:
            print(f" | ⚠️  Anomalies: {len(anomalies)}")
        else:
            print(" | ✅ Normal")
           
        # Performance status
        improvement_status = "🔄 Monitoring"
        if self.performance_monitor.wait_count == 0:
            improvement_status = "🎯 Improving!"
        elif self.performance_monitor.wait_count > self.performance_monitor.patience // 2:
            improvement_status = f"⏳ No improvement for {self.performance_monitor.wait_count} steps"
           
        print(f"  Best Loss: {self.performance_monitor.best_loss:.6f} | Status: {improvement_status}")
           
        # Log metrics
        for key, value in metrics.items():
            self.metrics_history[key].append((step, value))
           
        if self.enable_wandb and wandb.run is not None:
            wandb.log(metrics, step=step)
   
    def _get_grad_norm(self, model) -> Optional[float]:
        """Calculate gradient norm"""
        total_norm = 0
        param_count = 0
       
        for p in model.parameters():
            if p.grad is not None:
                param_norm = p.grad.data.norm(2)
                total_norm += param_norm.item() ** 2
                param_count += 1
               
        if param_count > 0:
            return (total_norm ** (1. / 2))
        return None
   
    def _check_anomalies(self, loss: float, grad_norm: Optional[float], step: int) -> List[str]:
        """Check for training anomalies"""
        anomalies = []
       
        # Loss anomalies
        if len(self.performance_monitor.loss_history) > 10:
            recent_losses = self.performance_monitor.loss_history[-10:]
            loss_mean = np.mean(recent_losses)
            loss_std = np.std(recent_losses)
           
            if loss > loss_mean + 3 * loss_std:
                anomalies.append(f"Loss spike: {loss:.4f} (mean: {loss_mean:.4f})")
               
        # Gradient anomalies
        if grad_norm is not None:
            if grad_norm > self.grad_norm_threshold:
                anomalies.append(f"High gradient norm: {grad_norm:.4f}")
            elif grad_norm < 1e-8:
                anomalies.append(f"Very low gradient norm: {grad_norm:.8f}")
               
        # Log anomalies with better formatting
        if anomalies:
            print(f"  🚨 ANOMALIES DETECTED:")
            for anomaly in anomalies:
                print(f"    - {anomaly}")
           
        return anomalies
   
    def _flatten_dict(self, d, parent_key='', sep='_'):
        """Flatten nested dictionary"""
        items = []
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(self._flatten_dict(v, new_key, sep=sep).items())
            elif isinstance(v, (list, tuple)):
                if len(v) > 0 and isinstance(v[0], (int, float)):
                    items.append((f"{new_key}_mean", np.mean(v)))
                    items.append((f"{new_key}_std", np.std(v)))
            else:
                items.append((new_key, v))
        return dict(items)

class FineTuningJobDB:
    """In-memory database for storing and managing FineTuningJob objects."""

    def __init__(self):
        self._jobs: dict[str, FineTuningJob] = {}
        self._counter = 0

    def create_job(self, fine_tuning_job: FineTuningJob) -> FineTuningJob:
        """Create and store a new fine-tuning job."""
        # Generate a unique ID if not provided or if it's a temporary ID
        if not fine_tuning_job.id or fine_tuning_job.id == "temp-id":
            self._counter += 1
            fine_tuning_job.id = f"ftjob-{int(time.time())}-{self._counter}"

        # Store the job
        self._jobs[fine_tuning_job.id] = fine_tuning_job
        logging.info(f"📝 Created job {fine_tuning_job.id} in database")
        return fine_tuning_job

    def get_job(self, job_id: str) -> FineTuningJob | None:
        """Retrieve a fine-tuning job by ID."""
        job = self._jobs.get(job_id)
        if job:
            logging.info(f"📖 Retrieved job {job_id} from database")
        else:
            logging.warning(f"⚠️  Job {job_id} not found in database")
        return job

    def update_job(
        self, job_id: str, fine_tuning_job: FineTuningJob
    ) -> FineTuningJob | None:
        """Update an existing fine-tuning job."""
        if job_id in self._jobs:
            self._jobs[job_id] = fine_tuning_job
            logging.info(f"📝 Updated job {job_id} in database")
            return fine_tuning_job
        else:
            logging.error(f"❌ Cannot update job {job_id}: not found in database")
            return None

    def list_jobs(self) -> dict[str, FineTuningJob]:
        """List all jobs from the database."""
        logging.info(f"📋 Listed {len(self._jobs)} jobs from database")
        return self._jobs.copy()

    def delete_job(self, job_id: str) -> bool:
        """Delete a fine-tuning job by ID."""
        if job_id in self._jobs:
            del self._jobs[job_id]
            logging.info(f"🗑️  Deleted job {job_id} from database")
            return True
        else:
            logging.warning(f"⚠️  Cannot delete job {job_id}: not found in database")
            return False

    def clear(self):
        """Clear all jobs from the database."""
        count = len(self._jobs)
        self._jobs.clear()
        logging.info(f"🧹 Cleared {count} jobs from database")

# Global database instance
fine_tuning_db = FineTuningJobDB()

class UnifiedFineTuner:
    """Enhanced unified fine-tuning class with comprehensive monitoring and OpenAI API compatibility."""

    def __init__(
        self,
        train_dataset: Any,
        fine_tuning_job: FineTuningJob,
        peft_method: str = PEFT_METHOD_QLORA,
        max_steps: int = 10,
        eval_steps: int = 5,
    ):
        """Initialize the enhanced unified fine-tuner.

        Args:
            train_dataset: Pre-prepared training dataset
            fine_tuning_job: OpenAI FineTuningJob object containing all configuration
            peft_method: PEFT configuration string (none, lora, qlora)
            max_steps: Maximum training steps
            eval_steps: Steps between evaluations
        """
        self.train_dataset = train_dataset
        self.fine_tuning_job = fine_tuning_job
        self.peft_method = peft_method
        self.max_steps = max_steps
        self.eval_steps = eval_steps

        # Extract configuration from FineTuningJob
        self.method = (
            fine_tuning_job.method.type
            if fine_tuning_job.method
            else METHOD_TYPE_SUPERVISED
        )
        self.model_id = fine_tuning_job.model
        self.training_file = fine_tuning_job.training_file
        self.validation_file = fine_tuning_job.validation_file
        self.seed = fine_tuning_job.seed
        self.metadata = fine_tuning_job.metadata

        # Enhanced dataset type detection
        self.dataset_type, self.has_vision = self._detect_dataset_type_enhanced()

        # Initialize state
        self.processor = None
        self.tokenizer = None
        self.model = None
        self.trainer = None
        self.eval_dataset = None

        # Enhanced monitoring configuration
        self.monitoring_config = MONITORING_CONFIG.copy()
        self.monitoring_config['enable_wandb'] = False  # Disable by default to avoid API key issues

        # Setup enhanced monitoring if requested
        if self.monitoring_config.get('enable_wandb', False):
            self._setup_wandb()

    def _detect_dataset_type_enhanced(self) -> tuple[str, bool]:
        """Enhanced dataset type detection that works for any dataset structure."""
        if not self.train_dataset or len(self.train_dataset) == 0:
            return "text_only", False

        # Check multiple examples for more robust detection
        sample_size = min(5, len(self.train_dataset))
        vision_indicators = []
       
        for i in range(sample_size):
            example = self.train_dataset[i]
            has_vision_this_example = False
           
            # Check for direct vision indicators
            vision_keys = [
                "video link", "videos", "image", "video", "pixel_values",
                "image_path", "video_path", "image_url", "video_url"
            ]
           
            for key in vision_keys:
                if key in example:
                    has_vision_this_example = True
                    break
           
            # Check messages content for vision elements
            if not has_vision_this_example and "messages" in example:
                messages = example["messages"]
                if isinstance(messages, str):
                    try:
                        messages = json.loads(messages)
                    except:
                        pass
               
                if isinstance(messages, list):
                    for message in messages:
                        if isinstance(message, dict):
                            content = message.get("content", [])
                            if isinstance(content, list):
                                for content_item in content:
                                    if isinstance(content_item, dict):
                                        content_type = content_item.get("type", "")
                                        if content_type in ["video", "image"]:
                                            has_vision_this_example = True
                                            break
                                if has_vision_this_example:
                                    break
           
            vision_indicators.append(has_vision_this_example)
       
        # Determine overall dataset type
        vision_ratio = sum(vision_indicators) / len(vision_indicators)
       
        if vision_ratio > 0.5:
            dataset_type = "vision_mixed" if vision_ratio < 1.0 else "vision_only"
            has_vision = True
        elif vision_ratio > 0:
            dataset_type = "mixed"
            has_vision = True  # Has some vision data
        else:
            dataset_type = "text_only"
            has_vision = False
       
        logging.info(f"🔍 Enhanced dataset type detected: {dataset_type} (vision ratio: {vision_ratio:.2f})")
        return dataset_type, has_vision

    def _setup_wandb(self):
        """Setup Weights & Biases monitoring"""
        try:
            model_name = self.model_id.split("/")[-1]
            run_name = f"{model_name}-{self.dataset_type}-{self.method}-{self.peft_method}"
           
            wandb.init(
                project="enhanced-unified-finetuning",
                name=run_name,
                config={
                    "model_id": self.model_id,
                    "method": self.method,
                    "peft_method": self.peft_method,
                    "dataset_type": self.dataset_type,
                    "has_vision": self.has_vision,
                    "dataset_size": len(self.train_dataset),
                    "max_steps": self.max_steps,
                    "eval_steps": self.eval_steps,
                    "batch_size": self._get_batch_size(),
                    "learning_rate": self._get_learning_rate(),
                    "num_epochs": self._get_num_epochs(),
                    **self.monitoring_config
                },
                tags=[
                    "unified-finetuning",
                    self.dataset_type,
                    self.method,
                    self.peft_method,
                    "enhanced-monitoring"
                ]
            )
            logging.info("✅ Weights & Biases initialized")
        except Exception as e:
            logging.warning(f"Failed to initialize Weights & Biases: {e}")
            self.monitoring_config['enable_wandb'] = False

    def _create_evaluation_dataset(self) -> Optional[Dataset]:
        """Create evaluation dataset from training data"""
        try:
            # Create evaluation split from training data
            if len(self.train_dataset) >= 10:
                # Use 20% for evaluation, but at least 2 examples
                eval_size = max(2, int(len(self.train_dataset) * 0.2))
                eval_indices = list(range(len(self.train_dataset)))[-eval_size:]
                eval_dataset = self.train_dataset.select(eval_indices)
                logging.info(f"✅ Created evaluation dataset with {len(eval_dataset)} examples")
                return eval_dataset
            elif len(self.train_dataset) >= 3:
                # For very small datasets, use the last example for eval
                eval_dataset = self.train_dataset.select([len(self.train_dataset) - 1])
                logging.info(f"✅ Created minimal evaluation dataset with {len(eval_dataset)} examples")
                return eval_dataset
            else:
                logging.warning("Dataset too small for evaluation split")
                return None
               
        except Exception as e:
            logging.warning(f"Failed to create evaluation dataset: {e}")
            return None

    def _get_batch_size(self) -> int:
        """Get batch size from FineTuningJob method configuration."""
        method = self.fine_tuning_job.method

        if not method:
            return 1

        # Extract based on method type
        if method.type == METHOD_TYPE_SUPERVISED and method.supervised:
            batch_size = getattr(method.supervised.hyperparameters, "batch_size", 1)
            # Handle string values like "auto" or None
            if isinstance(batch_size, str) or batch_size is None:
                batch_size = 1
            return int(batch_size)
        elif method.type == METHOD_TYPE_DPO and method.dpo:
            batch_size = getattr(method.dpo.hyperparameters, "batch_size", 1)
            # Handle string values like "auto" or None
            if isinstance(batch_size, str) or batch_size is None:
                batch_size = 1
            return int(batch_size)
        else:
            return 1

    def _get_learning_rate(self) -> float:
        """Get learning rate from FineTuningJob method configuration."""
        method = self.fine_tuning_job.method

        if not method:
            return 5e-5

        # Extract based on method type
        if method.type == METHOD_TYPE_SUPERVISED and method.supervised:
            multiplier = getattr(
                method.supervised.hyperparameters, "learning_rate_multiplier", 1.0
            )
            # Handle string values like "auto" or None
            if isinstance(multiplier, str) or multiplier is None:
                multiplier = 1.0
            return float(multiplier) * 5e-5
        elif method.type == METHOD_TYPE_DPO and method.dpo:
            multiplier = getattr(
                method.dpo.hyperparameters, "learning_rate_multiplier", 1.0
            )
            # Handle string values like "auto" or None
            if isinstance(multiplier, str) or multiplier is None:
                multiplier = 1.0
            return float(multiplier) * 5e-5
        else:
            return 5e-5

    def _get_num_epochs(self) -> int:
        """Get number of epochs from FineTuningJob method configuration."""
        method = self.fine_tuning_job.method

        if not method:
            return 3  # Default to 3 epochs

        # Extract based on method type
        if method.type == METHOD_TYPE_SUPERVISED and method.supervised:
            n_epochs = getattr(method.supervised.hyperparameters, "n_epochs", 3)
            # Handle string values like "auto" or None
            if isinstance(n_epochs, str) or n_epochs is None:
                n_epochs = 3  # Map "auto" to 3 epochs
            return int(n_epochs)
        elif method.type == METHOD_TYPE_DPO and method.dpo:
            n_epochs = getattr(method.dpo.hyperparameters, "n_epochs", 3)
            # Handle string values like "auto" or None
            if isinstance(n_epochs, str) or n_epochs is None:
                n_epochs = 3  # Map "auto" to 3 epochs
            return int(n_epochs)
        else:
            return 3  # Default to 3 epochs

    def run_training(self) -> dict[str, Any]:
        """Run the enhanced training workflow with comprehensive monitoring."""
        logging.info("🚀 STARTING ENHANCED UNIFIED FINE-TUNING WORKFLOW")
        logging.info("=" * 80)
        logging.info(f"📊 Dataset type: {self.dataset_type} | Has vision: {self.has_vision}")
        logging.info(f"🎯 Method: {self.method} | PEFT: {self.peft_method}")

        try:
            self._load_processor_and_model()
            self._setup_enhanced_training()

            # Run the actual training
            logging.info("🔧 STEP 3: Running enhanced training...")

            # Check for checkpoints
            model_name = self.model_id.split("/")[-1]
            suffix = (
                f"_{getattr(self.fine_tuning_job, 'suffix', '')}"
                if getattr(self.fine_tuning_job, "suffix", None)
                else ""
            )
            output_dir = f"{OUTPUT_BASE_DIR}/{model_name}-{self.dataset_type}-{self.method}-{self.peft_method}{suffix}"

            checkpoints = glob.glob(f"{output_dir}/checkpoint-*")
            resume_checkpoint = None
            if checkpoints:
                checkpoints = sorted(checkpoints, key=lambda x: int(x.split("-")[-1]))
                resume_checkpoint = checkpoints[-1]
                logging.info(f"    🔄 Resuming from checkpoint: {resume_checkpoint}")
            else:
                logging.info("    🚀 Starting fresh training...")

            # Run training with enhanced monitoring
            logging.info(f"    📊 Training with {self.method.upper()} method and enhanced monitoring...")
            train_result = self.trainer.train(resume_from_checkpoint=resume_checkpoint)
            logging.info("    ✅ Enhanced training completed!")

            training_results = {
                "train_result": train_result,
                "output_dir": output_dir,
                "trainer": self.trainer,  # Include trainer to access log_history and monitoring data
            }

            # Enhanced evaluation
            logging.info("🔧 STEP 4: Running enhanced evaluation...")
            eval_results = {}
           
            if self.eval_dataset and hasattr(self.trainer, 'evaluate'):
                try:
                    eval_results = self.trainer.evaluate()
                    logging.info("    ✅ Model evaluation completed")
                   
                    # Log evaluation results
                    print("\n🎯 EVALUATION RESULTS:")
                    print("=" * 50)
                    for key, value in eval_results.items():
                        if isinstance(value, (int, float)):
                            print(f"  {key}: {value:.4f}")
                        else:
                            print(f"  {key}: {str(value)[:100]}")
                           
                except Exception as e:
                    logging.warning(f"Evaluation failed: {e}")

            # Memory and performance summary
            memory_summary = self.trainer.memory_tracker.get_memory_summary()
           
            print("\n💾 MEMORY USAGE SUMMARY:")
            print("=" * 50)
            for key, value in memory_summary.items():
                print(f"  {key}: {value:.2f}GB")

            # Disable gradient checkpointing for inference
            if hasattr(self.model, "gradient_checkpointing_disable"):
                self.model.gradient_checkpointing_disable()

            # Generate enhanced summary
            logging.info("🔧 STEP 5: Generating enhanced summary...")

            summary = {
                "model_id": self.model_id,
                "method": self.method,
                "peft_method": self.peft_method,
                "dataset_type": self.dataset_type,
                "has_vision": self.has_vision,
                "max_steps": self.max_steps,
                "batch_size": self._get_batch_size(),
                "learning_rate": self._get_learning_rate(),
                "num_epochs": self._get_num_epochs(),
                "dataset_size": len(self.train_dataset),
                "eval_dataset_size": len(self.eval_dataset) if self.eval_dataset else 0,
                "output_dir": output_dir,
                "train_result": train_result,  # Include for metrics extraction
                "final_step": train_result.global_step if hasattr(train_result, 'global_step') else self.max_steps,
                "best_loss": self.trainer.performance_monitor.best_loss,
                "total_anomalies": self.trainer.anomaly_count,
                **eval_results,
                **memory_summary,
            }

            # Add method-specific metrics
            if self.method == METHOD_TYPE_SUPERVISED and hasattr(self.model, "get_nb_trainable_parameters"):
                trainable_params = self.model.get_nb_trainable_parameters()
                summary["trainable_parameters"] = trainable_params

            # Log final summary to WandB
            if self.monitoring_config.get('enable_wandb', False) and wandb.run is not None:
                wandb.log({
                    "training/completed": True,
                    "training/final_summary": summary
                })

            logging.info("📊 ENHANCED FINAL SUMMARY:")
            logging.info("=" * 50)
            for key, value in summary.items():
                if key == "train_result":
                    continue  # Skip the complex train_result object in logging
                if isinstance(value, (int, float)):
                    logging.info(f"    - {key}: {value:.6f}" if isinstance(value, float) else f"    - {key}: {value}")
                else:
                    logging.info(f"    - {key}: {value}")

            return summary

        except Exception as e:
            logging.error(f"❌ Enhanced training failed: {e}")
            if self.monitoring_config.get('enable_wandb', False) and wandb.run is not None:
                wandb.log({
                    "training/failed": True,
                    "training/error": str(e)
                })
            raise
        finally:
            # Clean up WandB
            if self.monitoring_config.get('enable_wandb', False) and wandb.run is not None:
                wandb.finish()

    def _load_processor_and_model(self) -> None:
        """Load processor and model with enhanced configuration."""
        logging.info("🔧 STEP 1: Loading processor and model with enhanced configuration...")

        # Load SmolVLM2 processor with universal configuration
        logging.info(f"    📥 Loading processor from {self.model_id}")
        do_image_splitting = False  # Disable to avoid string indexing issues
       
        self.processor = AutoProcessor.from_pretrained(
            self.model_id, do_image_splitting=do_image_splitting
        )
        self.tokenizer = self.processor.tokenizer
       
        logging.info(f"    ✅ Processor loaded. Tokenizer vocab size: {len(self.tokenizer)}")
        logging.info(f"        do_image_splitting: {do_image_splitting}")
        logging.info(f"        dataset_type: {self.dataset_type}")
        logging.info(f"        has_vision: {self.has_vision}")

        # Load model based on PEFT configuration
        self._load_model()

        # Log memory usage
        initial_mem = torch.cuda.max_memory_allocated()
        logging.info(f"    📊 Initial GPU memory usage: {initial_mem / MEMORY_CONVERSION_FACTOR:.2f} GB")

    def _setup_enhanced_training(self) -> None:
        """Setup enhanced training configuration with comprehensive monitoring."""
        logging.info("🔧 STEP 2: Setting up enhanced training configuration...")

        # Create evaluation dataset
        self.eval_dataset = self._create_evaluation_dataset()

        if self.method == METHOD_TYPE_SUPERVISED:
            self._setup_enhanced_sft_training()
        else:
            self._setup_enhanced_dpo_training()

    def _setup_enhanced_sft_training(self) -> None:
        """Setup enhanced SFT training with monitoring."""
        logging.info("    ⚙️  Setting up enhanced SFT training...")

        # Create training arguments
        model_name = self.model_id.split("/")[-1]
        suffix = (
            f"_{getattr(self.fine_tuning_job, 'suffix', '')}"
            if getattr(self.fine_tuning_job, "suffix", None)
            else ""
        )
        output_dir = f"{OUTPUT_BASE_DIR}/{model_name}-{self.dataset_type}-{self.method}-{self.peft_method}{suffix}"

        training_args = TrainingArguments(
            output_dir=output_dir,
            num_train_epochs=self._get_num_epochs(),
            per_device_train_batch_size=self._get_batch_size(),
            per_device_eval_batch_size=self._get_batch_size(),
            gradient_accumulation_steps=1,
            warmup_steps=max(2, self.max_steps // 10),  # Dynamic warmup steps
            learning_rate=self._get_learning_rate(),
            weight_decay=0.01,
            logging_steps=1,  # Log every step for full monitoring
            eval_strategy="steps" if self.eval_dataset else "no",
            eval_steps=self.eval_steps if self.eval_dataset else None,
            save_strategy="steps",
            save_steps=self.eval_steps,
            save_total_limit=2,
            load_best_model_at_end=True if self.eval_dataset else False,
            metric_for_best_model="eval_loss" if self.eval_dataset else None,
            greater_is_better=False,
            max_steps=self.max_steps,
            optim="paged_adamw_8bit" if self.peft_method != PEFT_METHOD_NONE else "adamw_torch",
            bf16=True,
            remove_unused_columns=False,
            report_to=["tensorboard"] + (["wandb"] if self.monitoring_config.get('enable_wandb', False) else []),
            label_names=["labels"],
            dataloader_pin_memory=False,
            gradient_checkpointing=True,
            gradient_checkpointing_kwargs={"use_reentrant": False},
            prediction_loss_only=False,  # Enable generation metrics
        )

        # Create enhanced trainer
        self.trainer = EnhancedUniversalTrainer(
            model=self.model,
            args=training_args,
            data_collator=self._create_enhanced_sft_collate_fn(),
            train_dataset=self.train_dataset,
            eval_dataset=self.eval_dataset,
            tokenizer=self.tokenizer,
            monitoring_config=self.monitoring_config,
            enable_generation_metrics=self.monitoring_config.get('enable_generation_metrics', True),
            dataset_type=self.dataset_type,
        )

        logging.info("    ✅ Enhanced SFT trainer configured")

    def _setup_enhanced_dpo_training(self) -> None:
        """Setup enhanced DPO training with monitoring."""
        logging.info("    ⚙️  Setting up enhanced DPO training...")

        # Create DPO config
        model_name = self.model_id.split("/")[-1]
        suffix = (
            f"_{getattr(self.fine_tuning_job, 'suffix', '')}"
            if getattr(self.fine_tuning_job, "suffix", None)
            else ""
        )
        output_dir = f"{OUTPUT_BASE_DIR}/{model_name}-{self.dataset_type}-{self.method}-{self.peft_method}{suffix}"

        training_args = DPOConfig(
            output_dir=output_dir,
            bf16=True,
            gradient_checkpointing=True,
            per_device_train_batch_size=self._get_batch_size(),
            gradient_accumulation_steps=32,
            num_train_epochs=self._get_num_epochs(),
            dataset_num_proc=8,
            dataloader_num_workers=8,
            logging_steps=1,
            max_steps=self.max_steps,
            label_names=["labels"],
            save_steps=self.eval_steps,
            save_total_limit=2,
            report_to=["tensorboard"] + (["wandb"] if self.monitoring_config.get('enable_wandb', False) else []),
        )

        # Create DPO trainer (Note: This would need to be enhanced with monitoring for full support)
        peft_config = (
            getattr(self, "lora_config", None)
            if self.peft_method != PEFT_METHOD_NONE
            else None
        )

        self.trainer = DPOTrainer(
            model=self.model,
            ref_model=None,
            args=training_args,
            train_dataset=self.train_dataset,
            peft_config=peft_config,
        )

        logging.info("    ✅ Enhanced DPO trainer configured")

    def _load_model(self) -> None:
        """Load model with appropriate PEFT configuration."""
        logging.info(f"    📥 Loading model with {self.peft_method} configuration...")

        if self.peft_method == PEFT_METHOD_NONE:
            # Load model for full fine-tuning
            logging.info("        Using full fine-tuning (no PEFT)")
            self.model = self._load_base_model()

            # Smart parameter freezing based on dataset type
            if (
                not self.has_vision
                and hasattr(self.model, "model")
                and hasattr(self.model.model, "vision_model")
            ):
                frozen_params = sum(
                    param.numel()
                    for param in self.model.model.vision_model.parameters()
                )
                for param in self.model.model.vision_model.parameters():
                    param.requires_grad = False
                logging.info(
                    f"        🧊 Frozen {frozen_params} vision model parameters (text-only dataset detected)"
                )
            elif self.has_vision:
                logging.info("        🔓 Vision model kept trainable (vision dataset detected)")

            logging.info("        ✅ Model loaded for full fine-tuning")
        else:
            # Load model with PEFT configuration
            logging.info(f"        Using {self.peft_method.upper()}")

            # Create LoRA configuration
            lora_config = LoraConfig(
                task_type=TaskType.CAUSAL_LM,
                target_modules=SMOLVLM_TARGET_MODULES,
            )
            lora_config.inference_mode = False
            logging.info(
                f"        ✅ LoRA config created: {set(SMOLVLM_TARGET_MODULES)}"
            )

            # Create quantization config if QLoRA
            bnb_config = None
            if self.peft_method == PEFT_METHOD_QLORA:
                bnb_config = BitsAndBytesConfig(
                    load_in_4bit=True,
                    bnb_4bit_use_double_quant=True,
                    bnb_4bit_quant_type="nf4",
                    bnb_4bit_compute_dtype=torch.bfloat16,
                )
                logging.info(
                    "        ✅ Quantization config created: 4-bit NF4 with double quant"
                )

            # Load base model
            self.model = self._load_base_model(bnb_config)
            logging.info("        ✅ Base model loaded")

            # Store LoRA config for trainer
            self.lora_config = lora_config

            # Apply PEFT for SFT (DPO handles PEFT through trainer)
            if self.method == METHOD_TYPE_SUPERVISED:
                # Apply PEFT configuration for SFT training
                logging.info("        🔗 Applying PEFT for SFT training...")

                # Verify target modules exist in the model
                linear_modules = {
                    name.split(".")[-1]
                    for name, module in self.model.named_modules()
                    if isinstance(module, torch.nn.Linear)
                }
                expected_modules = set(SMOLVLM_TARGET_MODULES)
                found_modules = expected_modules.intersection(linear_modules)
                missing_modules = expected_modules - linear_modules

                logging.info(
                    f"        ✅ Target modules found: {sorted(found_modules)}"
                )
                if missing_modules:
                    logging.warning(
                        f"        ⚠️  Target modules missing: {sorted(missing_modules)}"
                    )

                if len(missing_modules) != 0:
                    raise RuntimeError(
                        f"Expected SmolVLM2 modules missing: {missing_modules}"
                    )
                logging.info(
                    "        🎯 All expected SmolVLM2 target modules confirmed present!"
                )

                # Apply PEFT in the correct order for SFT
                self.model.add_adapter(lora_config)
                self.model.enable_adapters()
                self.model = prepare_model_for_kbit_training(self.model)
                self.model = get_peft_model(self.model, lora_config)

                # Log trainable parameters
                trainable_params = self.model.get_nb_trainable_parameters()
                logging.info(f"        📊 Trainable parameters: {trainable_params}")
                logging.info("        ✅ PEFT applied for SFT training")
            else:
                logging.info("        ✅ LoRA config prepared for DPO trainer")

    def _load_base_model(self, quantization_config=None) -> AutoModelForImageTextToText:
        """Load base model with unified loading logic."""
        kwargs = {
            "pretrained_model_name_or_path": self.model_id,
            "torch_dtype": torch.bfloat16,
            "device_map": "auto",
        }
        if quantization_config:
            kwargs["quantization_config"] = quantization_config
        return AutoModelForImageTextToText.from_pretrained(**kwargs)

    def _create_enhanced_sft_collate_fn(self):
        """Create enhanced collate function for SFT training that works universally."""
        # Get special token IDs for masking
        image_token_id = None
        if hasattr(self.tokenizer, "additional_special_tokens_ids"):
            try:
                image_token_id = self.tokenizer.additional_special_tokens_ids[
                    self.tokenizer.additional_special_tokens.index("<image>")
                ]
            except (ValueError, AttributeError):
                image_token_id = None

        def enhanced_collate_fn(examples):
            """Enhanced SFT collate function with universal dataset support."""
            instances = []

            # Process each example with enhanced logic
            for example in examples:
                try:
                    # The dataset contains the messages field
                    messages = example["messages"]

                    # Try to use apply_chat_template if available and appropriate
                    if self.has_vision and hasattr(self.processor, 'apply_chat_template'):
                        try:
                            # For vision datasets, try the processor's chat template
                            tokenized = self.processor.apply_chat_template(
                                messages,
                                add_generation_prompt=False,
                                tokenize=True,
                                return_dict=True,
                                return_tensors="pt",
                            )
                           
                            # Move to GPU and correct dtype
                            instance = {
                                "input_ids": tokenized["input_ids"].to("cuda").long(),
                                "attention_mask": tokenized["attention_mask"].to("cuda").long(),
                            }
                           
                            # Handle pixel values if present
                            if "pixel_values" in tokenized:
                                instance["pixel_values"] = tokenized["pixel_values"]
                               
                            instances.append(instance)
                            continue
                           
                        except Exception as e:
                            logging.debug(f"Chat template failed, falling back to simple processing: {e}")

                    # Fallback: Create a simple conversation string
                    conversation = ""
                    for msg in messages:
                        role = msg["role"]
                        content = msg.get("content", "")
                       
                        # Handle structured content for vision models
                        if isinstance(content, list):
                            text_content = ""
                            for item in content:
                                if isinstance(item, dict) and item.get("type") == "text":
                                    text_content += item.get("text", "")
                            content = text_content
                       
                        if role == "user":
                            conversation += f"User: {content}\n"
                        elif role == "assistant":
                            # Handle tool calls
                            if "tool_calls" in msg:
                                tool_text = ""
                                for tool_call in msg["tool_calls"]:
                                    func_name = tool_call["function"]["name"]
                                    func_args = tool_call["function"]["arguments"]
                                    tool_text += f"{func_name}({func_args})"
                                conversation += f"Assistant: {tool_text}\n"
                            else:
                                conversation += f"Assistant: {content}\n"
                        elif role == "system":
                            conversation += f"System: {content}\n"

                    # Tokenize the conversation directly
                    tokenized = self.tokenizer(
                        conversation,
                        truncation=True,
                        padding=False,
                        return_tensors="pt",
                        add_special_tokens=True,
                    )

                    # Move to GPU and correct dtype
                    instance = {
                        "input_ids": tokenized["input_ids"].to("cuda").long(),
                        "attention_mask": tokenized["attention_mask"].to("cuda").long(),
                    }
                    instances.append(instance)
                   
                except Exception as e:
                    logging.warning(f"Failed to process example: {e}")
                    continue

            if not instances:
                raise ValueError("No valid instances found in batch")

            # Pad sequences
            input_ids = pad_sequence(
                [inst["input_ids"].squeeze(0) for inst in instances],
                batch_first=True,
                padding_value=self.tokenizer.pad_token_id,
            )
            attention_mask = pad_sequence(
                [inst["attention_mask"].squeeze(0) for inst in instances],
                batch_first=True,
                padding_value=0,
            )
            labels = pad_sequence(
                [inst["input_ids"].squeeze(0).clone() for inst in instances],
                batch_first=True,
                padding_value=-100,
            )

            # Mask special tokens
            if image_token_id is not None:
                labels[labels == image_token_id] = -100

            result = {
                "input_ids": input_ids,
                "attention_mask": attention_mask,
                "labels": labels,
            }

            # Handle pixel_values when present (for vision data)
            pvs = [
                inst.get("pixel_values")
                for inst in instances
                if inst.get("pixel_values") is not None
            ]
            if pvs:
                try:
                    result["pixel_values"] = torch.stack([pv.squeeze(0) for pv in pvs])
                except Exception as e:
                    logging.warning(f"Failed to stack pixel values: {e}")

            return result

        return enhanced_collate_fn

def _create_training_metrics_file(training_results: dict[str, Any]) -> str:
    """Create a training metrics CSV file from actual training data and register it in the files service.

    Args:
        training_results: Training results containing train_result from trainer

    Returns:
        File ID of the created metrics file

    Raises:
        ValueError: If no valid training metrics are found
    """
    # Import here to avoid circular imports
    try:
        from backend.services.files_service import DATA_DIR, FILES_METADATA
    except ImportError:
        # Handle case when running script directly
        import sys
        import os as os_module
        sys.path.insert(0, os_module.path.join(os_module.path.dirname(__file__), '..', '..'))
        from backend.services.files_service import DATA_DIR, FILES_METADATA

    # Extract real training metrics from the trainer's log history
    train_result = training_results.get("train_result")
    trainer = training_results.get("trainer")

    if not train_result:
        raise ValueError("No train_result found in training_results")

    # Check if train_result has the expected structure
    logging.info(f"train_result type: {type(train_result)}")
    logging.info(f"train_result attributes: {dir(train_result)}")

    # Also check trainer log_history
    if trainer:
        logging.info(f"trainer type: {type(trainer)}")
        logging.info(f"trainer has log_history: {hasattr(trainer, 'log_history')}")
        if hasattr(trainer, "log_history"):
            logging.info(
                f"trainer log_history length: {len(trainer.log_history) if trainer.log_history else 0}"
            )
            logging.info(
                f"trainer log_history sample: {trainer.log_history[:2] if trainer.log_history else 'empty'}"
            )

    # Extract metrics from the trainer's log history first (preferred)
    metrics_data = []

    if trainer and hasattr(trainer, "log_history") and trainer.log_history:
        logging.info("✅ Using trainer.log_history for metrics extraction")
        for i, entry in enumerate(trainer.log_history):
            logging.info(f"Log entry {i}: {entry}")
            if "train_loss" in entry:
                metrics_row = {
                    "step": entry.get("step", i + 1),
                    "train_loss": entry.get("train_loss", 0.0),
                }
                # Add epoch if available
                if "epoch" in entry:
                    metrics_row["epoch"] = entry["epoch"]
                # Add learning rate if available
                if "learning_rate" in entry:
                    metrics_row["learning_rate"] = entry["learning_rate"]
                # Add gradient norm if available
                if "grad_norm" in entry:
                    metrics_row["grad_norm"] = entry["grad_norm"]

                metrics_data.append(metrics_row)
                logging.info(f"Added metrics row: {metrics_row}")
    elif hasattr(train_result, "log_history") and train_result.log_history:
        logging.info("✅ Using train_result.log_history for metrics extraction")
        for i, entry in enumerate(train_result.log_history):
            logging.info(f"Log entry {i}: {entry}")
            if "train_loss" in entry:
                metrics_row = {
                    "step": entry.get("step", i + 1),
                    "train_loss": entry.get("train_loss", 0.0),
                }
                # Add epoch if available
                if "epoch" in entry:
                    metrics_row["epoch"] = entry["epoch"]
                # Add learning rate if available
                if "learning_rate" in entry:
                    metrics_row["learning_rate"] = entry["learning_rate"]
                # Add gradient norm if available
                if "grad_norm" in entry:
                    metrics_row["grad_norm"] = entry["grad_norm"]

                metrics_data.append(metrics_row)
                logging.info(f"Added metrics row: {metrics_row}")
    elif hasattr(train_result, "metrics") and hasattr(train_result, "training_loss"):
        logging.info(
            "⚠️ Using train_result direct fields (fallback - only final metrics)"
        )
        logging.info(f"train_result.metrics: {train_result.metrics}")
        logging.info(f"train_result.training_loss: {train_result.training_loss}")
        logging.info(f"train_result.global_step: {train_result.global_step}")

        # Create a single metrics entry from available data
        metrics_row = {
            "step": train_result.global_step,
            "train_loss": train_result.training_loss,
        }
        # Add any additional metrics from the metrics dict
        if train_result.metrics:
            for key, value in train_result.metrics.items():
                if key not in metrics_row:  # Don't override existing keys
                    metrics_row[key] = value

        metrics_data.append(metrics_row)
        logging.info(f"Added single metrics row: {metrics_row}")
    else:
        raise ValueError(
            f"train_result does not have expected metrics structure. Available attributes: {dir(train_result)}"
        )

    if not metrics_data:
        # Log what we actually found for debugging
        logging.error(
            f"No training metrics could be extracted. train_result: {train_result}"
        )
        if trainer:
            logging.error(
                f"trainer.log_history: {getattr(trainer, 'log_history', 'not available')}"
            )
        raise ValueError(
            "No training metrics could be extracted from train_result or trainer"
        )

    logging.info(
        f"📊 Successfully extracted {len(metrics_data)} training metrics entries"
    )

    # Generate a unique file ID
    file_id = f"file-{uuid.uuid4().hex[:8]}"
    filename = "training_metrics.csv"
    file_path = os.path.join(DATA_DIR, f"{file_id}-{filename}")

    # Determine CSV fieldnames from the data
    fieldnames = set()
    for row in metrics_data:
        fieldnames.update(row.keys())
    fieldnames = sorted(fieldnames)  # Consistent ordering

    # Write CSV file
    with open(file_path, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in metrics_data:
            writer.writerow(row)

    # Calculate file size
    file_size = os.path.getsize(file_path)

    # Register file in FILES_METADATA
    file_obj = {
        "id": file_id,
        "object": "file",
        "bytes": file_size,
        "created_at": int(time.time()),
        "filename": filename,
        "purpose": "fine-tune-results",
        "status": "uploaded",
        "status_details": None,
    }
    FILES_METADATA[file_id] = file_obj

    logging.info(
        f"✅ Created training metrics file: {file_id} -> {filename} ({len(metrics_data)} entries)"
    )
    return file_id

def validate_and_load_dataset(training_file_id: str):
    """Validate and load a dataset from JSONL file.

    Args:
        training_file_id: The training file ID

    Returns:
        The loaded and validated dataset
    """
    # Import here to avoid circular imports
    try:
        from backend.services.files_service import DATA_DIR, FILES_METADATA
    except ImportError:
        # Handle case when running script directly
        import sys
        import os as os_module
        sys.path.insert(0, os_module.path.join(os_module.path.dirname(__file__), '..', '..'))
        from backend.services.files_service import DATA_DIR, FILES_METADATA

    # Get file metadata
    file_metadata = FILES_METADATA.get(training_file_id)
    if not file_metadata:
        raise FileNotFoundError(
            f"Training file {training_file_id} not found in metadata"
        )

    # Determine the correct file path
    if "file_path" in file_metadata:
        jsonl_file_path = file_metadata["file_path"]
    else:
        # Construct path using files service pattern
        jsonl_file_path = os.path.join(
            DATA_DIR, f"{training_file_id}-{file_metadata['filename']}"
        )

    # Check if file exists
    if not os.path.exists(jsonl_file_path):
        raise FileNotFoundError(f"Dataset file not found: {jsonl_file_path}")

    # Load dataset from JSONL
    dataset = load_dataset("json", data_files=jsonl_file_path)
    train_dataset = dataset["train"]

    # Validate the dataset format
    if len(train_dataset) == 0:
        raise ValueError(f"Dataset is empty: {jsonl_file_path}")

    # Check that all examples have the messages field
    for i, example in enumerate(train_dataset):
        if "messages" not in example:
            raise ValueError(f"Example {i} missing 'messages' field: {example}")

        messages = example["messages"]
        if not isinstance(messages, list):
            raise ValueError(
                f"Example {i} 'messages' field is not a list: {type(messages)}"
            )

        # Validate each message
        for j, message in enumerate(messages):
            if not isinstance(message, dict):
                raise ValueError(
                    f"Example {i}, message {j} is not a dict: {type(message)}"
                )

            if "role" not in message:
                raise ValueError(f"Example {i}, message {j} missing 'role' field")

            role = message["role"]
            content = message.get("content")

            if role not in ["user", "assistant", "system"]:
                raise ValueError(f"Example {i}, message {j} has invalid role: {role}")

            # Assistant messages can have tool_calls instead of content
            if role == "assistant" and content is None and "tool_calls" in message:
                # This is valid - assistant message with only tool calls
                continue

            # All other messages must have content
            if content is None:
                raise ValueError(f"Example {i}, message {j} missing 'content' field")

            # For vision data, content can be a list or string
            # For text data, content should be a string
            if not isinstance(content, str | list):
                raise ValueError(
                    f"Example {i}, message {j} content is not string or list: {type(content)}"
                )

    logging.info(
        f"✅ Loaded and validated {len(train_dataset)} examples from {jsonl_file_path}"
    )
    return train_dataset

def create_fine_tuning_job(
    training_file_id: str,
    method_type: str = METHOD_TYPE_SUPERVISED,
    model: str = MODEL_ID,
) -> str:
    """Create a fine-tuning job with the specified method type and store it in the database."""

    if method_type == METHOD_TYPE_SUPERVISED:
        method = Method(
            type="supervised",
            supervised=SupervisedMethod(
                hyperparameters=SupervisedHyperparameters(
                    batch_size="auto", learning_rate_multiplier="auto", n_epochs="auto"
                )
            ),
        )
    elif method_type == METHOD_TYPE_DPO:
        method = Method(
            type="dpo",
            dpo=DpoMethod(
                hyperparameters=DpoHyperparameters(
                    batch_size=None,
                    beta=None,
                    learning_rate_multiplier=None,
                    n_epochs=None,
                )
            ),
        )
    else:
        raise ValueError(f"Unsupported method type: {method_type}")

    # Create the job object
    fine_tuning_job = FineTuningJob(
        id="temp-id",  # Temporary ID, will be replaced by database
        created_at=int(time.time()),
        model=model,
        object="fine_tuning.job",
        organization_id="org-demo",
        result_files=[],
        seed=42,
        status="queued",  # Start with queued status since dataset is prepared
        training_file=training_file_id,
        hyperparameters=Hyperparameters(),
        method=method,
    )

    # Store in database and get the generated ID
    stored_job = fine_tuning_db.create_job(fine_tuning_job)

    return stored_job.id

def run_fine_tuning_job(job_id: str, **kwargs) -> FineTuningJob:
    """Run a fine-tuning job with OpenAI API-compatible interface and enhanced monitoring."""
    import time

    logging.info(f"🔧 run_fine_tuning_job called for job {job_id}")

    # Retrieve the job from the database
    fine_tuning_job = fine_tuning_db.get_job(job_id)
    if not fine_tuning_job:
        logging.error(f"❌ Job {job_id} not found in database")
        raise ValueError(f"Job {job_id} not found in database")

    logging.info(f"📊 Found job {job_id} with status: {fine_tuning_job.status}")

    # Check job status
    if fine_tuning_job.status == "running":
        logging.error(f"❌ Job {job_id} is already running")
        raise ValueError("Resuming a fine-tuning job is not yet supported")
    elif fine_tuning_job.status not in ["queued"]:
        logging.error(
            f"❌ Job {job_id} cannot be run in status '{fine_tuning_job.status}' - expected 'queued'"
        )
        raise ValueError(
            f"Job {job_id} cannot be run in status '{fine_tuning_job.status}'"
        )

    # Update status to validating_files
    fine_tuning_job.status = "validating_files"
    fine_tuning_db.update_job(job_id, fine_tuning_job)
    logging.info(f"🔍 Job {job_id} status updated to 'validating_files'")

    # Validate dataset file and load it
    logging.info(f"📁 Starting dataset validation for job {job_id}")
    method_type = (
        fine_tuning_job.method.type
        if fine_tuning_job.method
        else METHOD_TYPE_SUPERVISED
    )
    logging.info(f"⚙️  Method type for job {job_id}: {method_type}")

    try:
        train_dataset = validate_and_load_dataset(fine_tuning_job.training_file)
        logging.info(f"✅ Dataset validation completed for job {job_id}")
    except Exception as e:
        logging.error(f"❌ Dataset validation failed for job {job_id}: {str(e)}")
        fine_tuning_job.status = "failed"
        fine_tuning_job.finished_at = int(time.time())
        fine_tuning_job.error = {
            "code": "dataset_validation_failed",
            "message": str(e),
            "param": None,
            "type": "server_error",
        }
        fine_tuning_db.update_job(job_id, fine_tuning_job)
        return fine_tuning_job

    # Update status to running
    fine_tuning_job.status = "running"
    fine_tuning_db.update_job(job_id, fine_tuning_job)
    logging.info(f"🔄 Job {job_id} status updated to 'running'")

    # Set random seed if provided
    if fine_tuning_job.seed is not None:
        torch.manual_seed(fine_tuning_job.seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed(fine_tuning_job.seed)

    # Determine PEFT method based on method type
    if method_type == METHOD_TYPE_SUPERVISED:
        peft_method = PEFT_METHOD_QLORA  # Default to QLoRA for supervised
    elif method_type == METHOD_TYPE_DPO:
        peft_method = PEFT_METHOD_LORA  # Default to LoRA for DPO
    else:
        peft_method = PEFT_METHOD_QLORA  # Default fallback

    # Extract training parameters from kwargs
    max_steps = kwargs.get("max_steps", 10)
    eval_steps = kwargs.get("eval_steps", max_steps // 2 if max_steps > 1 else 1)

    # Create enhanced fine-tuner instance with pre-prepared dataset
    fine_tuner = UnifiedFineTuner(
        train_dataset=train_dataset,
        fine_tuning_job=fine_tuning_job,
        peft_method=peft_method,
        max_steps=max_steps,
        eval_steps=eval_steps,
    )

    try:
        # Run enhanced training
        training_results = fine_tuner.run_training()

        # Create a training metrics CSV file for the result
        result_file_id = _create_training_metrics_file(training_results)

        # Update the original FineTuningJob object with results
        fine_tuning_job.status = "succeeded"
        fine_tuning_job.finished_at = int(time.time())
        fine_tuning_job.result_files = [result_file_id]
        fine_tuning_job.trained_tokens = training_results.get("total_flos", 0)

        # Update the job in the database
        fine_tuning_db.update_job(job_id, fine_tuning_job)
        logging.info(f"✅ Job {job_id} completed successfully with enhanced monitoring")

        return fine_tuning_job

    except Exception as e:
        # Handle training failure
        # Update the original FineTuningJob object with error information
        fine_tuning_job.status = "failed"
        fine_tuning_job.finished_at = int(time.time())
        fine_tuning_job.result_files = []
        fine_tuning_job.trained_tokens = 0

        # Add error information to the job
        fine_tuning_job.error = {
            "code": "training_failed",
            "message": str(e),
            "param": None,
            "type": "server_error",
        }

        # Update the job in the database
        fine_tuning_db.update_job(job_id, fine_tuning_job)
        logging.error(f"❌ Job {job_id} failed: {str(e)}")

        return fine_tuning_job

def cancel_job(job_id: str) -> FineTuningJob:
    """Cancel a fine-tuning job."""
    fine_tuning_job = fine_tuning_db.get_job(job_id)
    if not fine_tuning_job:
        raise ValueError(f"Job {job_id} not found in database")

    # Check if job can be cancelled
    if fine_tuning_job.status not in ["queued", "running"]:
        raise ValueError(
            f"Job {job_id} cannot be cancelled in status '{fine_tuning_job.status}'"
        )

    # Update status to cancelled
    fine_tuning_job.status = "cancelled"
    fine_tuning_job.finished_at = int(time.time())
    fine_tuning_db.update_job(job_id, fine_tuning_job)
    logging.info(f"🚫 Job {job_id} cancelled")

    return fine_tuning_job

def main():
    """Main function using OpenAI API spec types with enhanced monitoring."""
    # Build OpenAI API compatible job configuration
    training_file_ids = [
        "file-drone-training-default",
        "file-tiger-lab-video-feedback-default",
    ]

    for training_file_id in training_file_ids:
        method_type = METHOD_TYPE_SUPERVISED  # Switch back to SFT

        job_id = create_fine_tuning_job(training_file_id, method_type=method_type)

        print("🚀 Starting enhanced fine-tuning job with OpenAI API spec...")
        print(f"📋 Job ID: {job_id}")

        # Get initial job state
        initial_job = fine_tuning_db.get_job(job_id)
        print(f"🎯 Training file: {initial_job.training_file}")
        print(f"⚙️  Method: {initial_job.method.type}")
        print(f"📊 Status: {initial_job.status}")
        print(f"📅 Created at: {initial_job.created_at}")
        print(f"🔧 Model: {initial_job.model}")
        print("=" * 80)

        # Run enhanced fine-tuning job using the new API
        fine_tuning_job = run_fine_tuning_job(job_id)

        # Print summary
        print("\n🎉 Enhanced fine-tuning job completed!")
        print(f"📋 Job ID: {fine_tuning_job.id}")
        print(f"📊 Status: {fine_tuning_job.status}")
        print(f"📅 Created at: {fine_tuning_job.created_at}")
        print(f"🔧 Model: {fine_tuning_job.model}")
        print(f"📁 Result files: {fine_tuning_job.result_files}")
        print(f"⏰ Finished at: {getattr(fine_tuning_job, 'finished_at', 'Not finished')}")
        print(f"❌ Error: {getattr(fine_tuning_job, 'error', 'None')}")
        print(f"🔢 Trained tokens: {getattr(fine_tuning_job, 'trained_tokens', 'Not trained')}")

if __name__ == "__main__":
    main()
