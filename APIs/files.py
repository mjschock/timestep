from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from fastapi.responses import JSONResponse
from typing import Optional, List, Dict, Any
import json
import uuid
import os
from datetime import datetime, timezone

router = APIRouter()

# In-memory storage for files (replace with database in production)
files_storage = {}

class FileObject:
    def __init__(self, file: UploadFile, purpose: str):
        self.id = f"file-{uuid.uuid4().hex[:8]}"
        self.object = "file"
        self.bytes = len(file.file.read())
        file.file.seek(0)  # Reset file pointer
        self.created_at = datetime.now(timezone.utc)
        self.filename = file.filename
        self.purpose = purpose
        self.status = "processed"
        self.status_details = None
        
        # Store file content (in production, save to disk/database)
        self.content = file.file.read()

@router.post("/files")
async def upload_file(
    file: UploadFile = File(...),
    purpose: str = Form(...)
):
    """Upload a file"""
    
    # Validate purpose
    valid_purposes = ["fine-tune", "fine-tune-results", "assistants", "assistants_output"]
    if purpose not in valid_purposes:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid purpose '{purpose}'. Must be one of: {valid_purposes}"
        )
    
    # Validate file size (100MB limit)
    file.file.seek(0, 2)  # Seek to end
    file_size = file.file.tell()
    file.file.seek(0)  # Reset to beginning
    
    if file_size > 100 * 1024 * 1024:  # 100MB
        raise HTTPException(
            status_code=400,
            detail="File size exceeds 100MB limit"
        )
    
    # Create file object
    file_obj = FileObject(file, purpose)
    files_storage[file_obj.id] = file_obj
    
    return {
        "id": file_obj.id,
        "object": file_obj.object,
        "bytes": file_obj.bytes,
        "created_at": int(file_obj.created_at.timestamp()),
        "filename": file_obj.filename,
        "purpose": file_obj.purpose,
        "status": file_obj.status,
        "status_details": file_obj.status_details
    }

@router.get("/files")
async def list_files(purpose: Optional[str] = None, limit: Optional[int] = None):
    """List files"""
    files = list(files_storage.values())
    
    if purpose:
        files = [f for f in files if f.purpose == purpose]
    
    if limit:
        files = files[:limit]
    
    return {
        "object": "list",
        "data": [
            {
                "id": file_obj.id,
                "object": file_obj.object,
                "bytes": file_obj.bytes,
                "created_at": int(file_obj.created_at.timestamp()),
                "filename": file_obj.filename,
                "purpose": file_obj.purpose,
                "status": file_obj.status,
                "status_details": file_obj.status_details
            }
            for file_obj in files
        ]
    }

@router.get("/files/{file_id}")
async def retrieve_file(file_id: str):
    """Retrieve a file"""
    if file_id not in files_storage:
        raise HTTPException(status_code=404, detail="File not found")
    
    file_obj = files_storage[file_id]
    
    return {
        "id": file_obj.id,
        "object": file_obj.object,
        "bytes": file_obj.bytes,
        "created_at": int(file_obj.created_at.timestamp()),
        "filename": file_obj.filename,
        "purpose": file_obj.purpose,
        "status": file_obj.status,
        "status_details": file_obj.status_details
    }

@router.delete("/files/{file_id}")
async def delete_file(file_id: str):
    """Delete a file"""
    if file_id not in files_storage:
        raise HTTPException(status_code=404, detail="File not found")
    
    file_obj = files_storage.pop(file_id)
    
    return {
        "id": file_obj.id,
        "object": "file",
        "deleted": True
    }

@router.get("/files/{file_id}/content")
async def retrieve_file_content(file_id: str):
    """Retrieve file content"""
    if file_id not in files_storage:
        raise HTTPException(status_code=404, detail="File not found")
    
    file_obj = files_storage[file_id]
    
    # In production, read from disk/database
    return JSONResponse(
        content=file_obj.content,
        headers={
            "Content-Type": "application/octet-stream",
            "Content-Disposition": f'attachment; filename="{file_obj.filename}"'
        }
    )