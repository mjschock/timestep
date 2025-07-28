#!/usr/bin/env python3
"""
OpenAI RFT-compatible training script for SmolVLA
Command-line interface for RFT fine-tuning
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import Optional

from smolvla_rft_trainer import RFTConfig, train_smolvla_rft

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description="OpenAI RFT-compatible training for SmolVLA",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    
    # Model configuration
    parser.add_argument(
        "--model_name",
        type=str,
        default="HuggingFaceTB/SmolVLA-256M-Video-Instruct",
        help="SmolVLA model name to use for RFT training"
    )
    
    # Checkpoint configuration
    parser.add_argument(
        "--checkpoint_path",
        type=str,
        default=None,
        help="Path to base model checkpoint (from standard training)"
    )
    
    # Output configuration
    parser.add_argument(
        "--output_dir",
        type=str,
        default="outputs/rft/smolvla_rft",
        help="Directory to save RFT-trained model"
    )
    
    # RFT configuration
    parser.add_argument(
        "--rft_iterations",
        type=int,
        default=1000,
        help="Number of RFT training iterations"
    )
    
    parser.add_argument(
        "--training_examples",
        type=int,
        default=50,
        help="Number of training examples to use (OpenAI: 'dozens')"
    )
    
    parser.add_argument(
        "--validation_examples",
        type=int,
        default=20,
        help="Number of validation examples"
    )
    
    parser.add_argument(
        "--responses_per_state",
        type=int,
        default=4,
        help="Number of action candidates to generate per state"
    )
    
    parser.add_argument(
        "--grader_weight",
        type=float,
        default=1.0,
        help="Weight for grader vs base policy"
    )
    
    # Grader configuration
    parser.add_argument(
        "--grader_type",
        type=str,
        default="expert_demonstration",
        choices=["expert_demonstration", "multi_objective"],
        help="Type of grader to use"
    )
    
    parser.add_argument(
        "--task_type",
        type=str,
        default="manipulation",
        choices=["manipulation", "navigation"],
        help="Type of robotics task"
    )
    
    # OpenAI API configuration
    parser.add_argument(
        "--use_openai_api",
        action="store_true",
        help="Use OpenAI API for LLM-based grading"
    )
    
    parser.add_argument(
        "--grader_model",
        type=str,
        default="gpt-4o",
        help="OpenAI model to use for grading (if use_openai_api=True)"
    )
    
    # Training settings
    parser.add_argument(
        "--learning_rate",
        type=float,
        default=1e-5,
        help="Learning rate for RFT training"
    )
    
    parser.add_argument(
        "--batch_size",
        type=int,
        default=8,
        help="Batch size for training"
    )
    
    parser.add_argument(
        "--log_freq",
        type=int,
        default=10,
        help="Frequency of logging (iterations)"
    )
    
    parser.add_argument(
        "--save_freq",
        type=int,
        default=100,
        help="Frequency of saving checkpoints (iterations)"
    )
    
    # Logging and monitoring
    parser.add_argument(
        "--wandb_enable",
        action="store_true",
        help="Enable Weights & Biases logging"
    )
    
    parser.add_argument(
        "--wandb_project",
        type=str,
        default="smolvla_rft",
        help="Weights & Biases project name"
    )
    
    parser.add_argument(
        "--wandb_run_name",
        type=str,
        default=None,
        help="Weights & Biases run name"
    )
    
    # Verbosity
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )
    
    return parser.parse_args()


def setup_wandb(args):
    """Setup Weights & Biases logging if enabled"""
    if args.wandb_enable:
        try:
            import wandb
            wandb.init(
                project=args.wandb_project,
                name=args.wandb_run_name,
                config=vars(args)
            )
            logger.info(f"📊 Weights & Biases logging enabled: {args.wandb_project}")
        except ImportError:
            logger.warning("Weights & Biases not installed. Install with: pip install wandb")
            args.wandb_enable = False


def validate_args(args):
    """Validate command line arguments"""
    # Check if checkpoint exists if provided
    if args.checkpoint_path and not Path(args.checkpoint_path).exists():
        raise ValueError(f"Checkpoint path does not exist: {args.checkpoint_path}")
    
    # Validate task type and grader type compatibility
    if args.task_type == "navigation" and args.grader_type == "expert_demonstration":
        logger.warning("Navigation task with expert demonstration grader may not be optimal")
    
    # Validate OpenAI API settings
    if args.use_openai_api:
        try:
            import openai
            # Check if API key is set
            if not openai.api_key:
                logger.warning("OpenAI API key not set. Set OPENAI_API_KEY environment variable")
        except ImportError:
            raise ValueError("OpenAI API not installed. Install with: pip install openai")
    
    logger.info("✅ Arguments validated successfully")


def create_rft_config(args) -> RFTConfig:
    """Create RFT configuration from command line arguments"""
    config = RFTConfig(
        training_examples=args.training_examples,
        validation_examples=args.validation_examples,
        rft_iterations=args.rft_iterations,
        responses_per_state=args.responses_per_state,
        grader_weight=args.grader_weight,
        grader_type=args.grader_type,
        task_type=args.task_type,
        use_openai_api=args.use_openai_api,
        grader_model=args.grader_model,
        learning_rate=args.learning_rate,
        batch_size=args.batch_size,
        log_freq=args.log_freq,
        save_freq=args.save_freq
    )
    
    return config


def main():
    """Main training function"""
    # Parse arguments
    args = parse_args()
    
    # Setup logging level
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Validate arguments
    validate_args(args)
    
    # Setup Weights & Biases if enabled
    setup_wandb(args)
    
    # Create RFT configuration
    config = create_rft_config(args)
    
    # Log configuration
    logger.info("🚀 Starting SmolVLA RFT training with configuration:")
    logger.info(f"  Model: {args.model_name}")
    logger.info(f"  Checkpoint: {args.checkpoint_path}")
    logger.info(f"  Output Directory: {args.output_dir}")
    logger.info(f"  RFT Iterations: {config.rft_iterations}")
    logger.info(f"  Training Examples: {config.training_examples}")
    logger.info(f"  Grader Type: {config.grader_type}")
    logger.info(f"  Task Type: {config.task_type}")
    logger.info(f"  Learning Rate: {config.learning_rate}")
    
    try:
        # Run RFT training
        policy = train_smolvla_rft(
            model_name=args.model_name,
            checkpoint_path=args.checkpoint_path,
            output_dir=args.output_dir,
            config=config
        )
        
        logger.info("✅ RFT training completed successfully!")
        logger.info(f"💾 Model saved to: {args.output_dir}")
        
        # Log final metrics if wandb is enabled
        if args.wandb_enable:
            import wandb
            wandb.finish()
        
        return 0
        
    except Exception as e:
        logger.error(f"❌ RFT training failed: {e}")
        if args.wandb_enable:
            import wandb
            wandb.finish()
        return 1


if __name__ == "__main__":
    sys.exit(main())