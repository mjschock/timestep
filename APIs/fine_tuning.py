from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from fastapi.responses import JSONResponse
from typing import Optional, List, Dict, Any
import json
import uuid
from datetime import datetime, timezone

router = APIRouter()

# In-memory storage for fine-tuning jobs (replace with database in production)
fine_tuning_jobs = {}

class FineTuningJob:
    def __init__(self, model: str, training_file: str, **kwargs):
        self.id = f"ft-{uuid.uuid4().hex[:8]}"
        self.model = model
        self.training_file = training_file
        self.created_at = datetime.now(timezone.utc)
        self.status = "validating_files"
        self.finished_at = None
        self.trained_tokens = None
        self.error = None
        self.result_files = []
        self.validation_file = kwargs.get("validation_file")
        self.hyperparameters = kwargs.get("hyperparameters", {})
        self.suffix = kwargs.get("suffix", "")
        self.object = "fine_tuning.job"

@router.post("/fine_tuning/jobs")
async def create_fine_tuning_job(
    model: str = Form(...),
    training_file: str = Form(...),
    validation_file: Optional[str] = Form(None),
    hyperparameters: Optional[str] = Form(None),
    suffix: Optional[str] = Form(None)
):
    """Create a fine-tuning job"""
    
    # Validate model
    if not model.startswith("SmolVLM2"):
        raise HTTPException(
            status_code=400,
            detail=f"Model '{model}' is not supported. Only SmolVLM2 models are supported for local fine-tuning."
        )
    
    # Parse hyperparameters
    hyperparams = {}
    if hyperparameters:
        try:
            hyperparams = json.loads(hyperparameters)
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="Invalid hyperparameters JSON")
    
    # Create job
    job = FineTuningJob(
        model=model,
        training_file=training_file,
        validation_file=validation_file,
        hyperparameters=hyperparams,
        suffix=suffix or ""
    )
    
    fine_tuning_jobs[job.id] = job
    
    # Simulate job progression
    job.status = "running"
    
    return {
        "id": job.id,
        "object": job.object,
        "model": job.model,
        "created_at": int(job.created_at.timestamp()),
        "finished_at": job.finished_at,
        "fine_tuned_model": None,
        "organization_id": "org-local",
        "result_files": job.result_files,
        "status": job.status,
        "validation_file": job.validation_file,
        "training_file": job.training_file,
        "trained_tokens": job.trained_tokens,
        "error": job.error,
        "hyperparameters": job.hyperparameters,
        "suffix": job.suffix
    }

@router.get("/fine_tuning/jobs")
async def list_fine_tuning_jobs(limit: Optional[int] = None):
    """List fine-tuning jobs"""
    jobs = list(fine_tuning_jobs.values())
    
    if limit:
        jobs = jobs[:limit]
    
    return {
        "object": "list",
        "data": [
            {
                "id": job.id,
                "object": job.object,
                "model": job.model,
                "created_at": int(job.created_at.timestamp()),
                "finished_at": job.finished_at,
                "fine_tuned_model": None,
                "organization_id": "org-local",
                "result_files": job.result_files,
                "status": job.status,
                "validation_file": job.validation_file,
                "training_file": job.training_file,
                "trained_tokens": job.trained_tokens,
                "error": job.error,
                "hyperparameters": job.hyperparameters,
                "suffix": job.suffix
            }
            for job in jobs
        ]
    }

@router.get("/fine_tuning/jobs/{job_id}")
async def retrieve_fine_tuning_job(job_id: str):
    """Retrieve a fine-tuning job"""
    if job_id not in fine_tuning_jobs:
        raise HTTPException(status_code=404, detail="Fine-tuning job not found")
    
    job = fine_tuning_jobs[job_id]
    
    return {
        "id": job.id,
        "object": job.object,
        "model": job.model,
        "created_at": int(job.created_at.timestamp()),
        "finished_at": job.finished_at,
        "fine_tuned_model": None,
        "organization_id": "org-local",
        "result_files": job.result_files,
        "status": job.status,
        "validation_file": job.validation_file,
        "training_file": job.training_file,
        "trained_tokens": job.trained_tokens,
        "error": job.error,
        "hyperparameters": job.hyperparameters,
        "suffix": job.suffix
    }

@router.post("/fine_tuning/jobs/{job_id}/cancel")
async def cancel_fine_tuning_job(job_id: str):
    """Cancel a fine-tuning job"""
    if job_id not in fine_tuning_jobs:
        raise HTTPException(status_code=404, detail="Fine-tuning job not found")
    
    job = fine_tuning_jobs[job_id]
    
    if job.status in ["succeeded", "failed", "cancelled"]:
        raise HTTPException(
            status_code=400,
            detail=f"Cannot cancel job in '{job.status}' status"
        )
    
    job.status = "cancelled"
    job.finished_at = datetime.now(timezone.utc)
    
    return {
        "id": job.id,
        "object": job.object,
        "model": job.model,
        "created_at": int(job.created_at.timestamp()),
        "finished_at": int(job.finished_at.timestamp()),
        "fine_tuned_model": None,
        "organization_id": "org-local",
        "result_files": job.result_files,
        "status": job.status,
        "validation_file": job.validation_file,
        "training_file": job.training_file,
        "trained_tokens": job.trained_tokens,
        "error": job.error,
        "hyperparameters": job.hyperparameters,
        "suffix": job.suffix
    }