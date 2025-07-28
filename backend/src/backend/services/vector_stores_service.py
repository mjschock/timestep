# mypy: ignore-errors
import uuid
from datetime import datetime
from typing import Any

import numpy as np
from fastapi import HTTPException
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class VectorStore:
    """
    Adapted from https://github.com/MadcowD/ell/blob/main/examples/rag/rag.py
    """

    def __init__(self, vectorizer, tfidf_matrix, documents, metadata=None) -> None:
        self.vectorizer = vectorizer
        self.tfidf_matrix = tfidf_matrix
        self.documents = documents
        self.metadata = metadata or []

    @classmethod
    def from_documents(
        cls, documents: list[str], metadata: list[dict] | None = None
    ) -> "VectorStore":
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(documents)
        return cls(vectorizer, tfidf_matrix, documents, metadata)

    def retrieve_with_scores(self, query: str, k: int = 2) -> list[dict]:
        query_vector = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vector, self.tfidf_matrix).flatten()
        top_k_indices = np.argsort(similarities)[-k:][::-1]
        return [
            {
                "document": self.documents[i],
                "relevance": float(similarities[i]),
                "metadata": (
                    self.metadata[i] if self.metadata and i < len(self.metadata) else {}
                ),
            }
            for i in top_k_indices
        ]

    def retrieve_context(self, query: str, k: int = 2) -> str:
        documents = self.retrieve_with_scores(query, k)
        return "\n".join([item["document"] for item in documents])

    def add_documents(
        self, new_documents: list[str], new_metadata: list[dict] | None = None
    ) -> None:
        """Add new documents to the vector store"""
        if new_metadata is None:
            new_metadata = [{} for _ in new_documents]

        # Combine existing and new documents
        all_documents = self.documents + new_documents
        all_metadata = self.metadata + new_metadata

        # Re-fit the vectorizer with all documents
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self.vectorizer.fit_transform(all_documents)
        self.documents = all_documents
        self.metadata = all_metadata


# Global storage for vector stores - singleton pattern
VECTOR_STORES: dict[str, dict[str, Any]] = {}


class VectorStoresService:
    def __init__(self) -> None:
        # Use global storage instead of instance storage
        self.vector_stores = VECTOR_STORES

    def list_vector_stores(
        self,
        limit: int = 20,
        order: str = "desc",
        after: str | None = None,
        before: str | None = None,
    ):
        """List all vector stores"""
        stores = list(self.vector_stores.values())

        # Apply pagination
        if after:
            stores = [s for s in stores if s["id"] > after]
        if before:
            stores = [s for s in stores if s["id"] < before]

        # Apply ordering
        stores.sort(key=lambda x: x["created_at"], reverse=(order == "desc"))

        # Apply limit
        stores = stores[:limit]

        return {
            "object": "list",
            "data": stores,
            "first_id": stores[0]["id"] if stores else None,
            "last_id": stores[-1]["id"] if stores else None,
            "has_more": len(stores) == limit,
        }

    def create_vector_store(self, name: str, metadata: dict | None = None):
        """Create a new vector store"""
        vector_store_id = f"vs_{uuid.uuid4().hex}"

        vector_store = {
            "id": vector_store_id,
            "object": "vector_store",
            "name": name,
            "metadata": metadata or {},
            "created_at": datetime.utcnow().isoformat(),
            "file_counts": {
                "in_progress": 0,
                "completed": 0,
                "failed": 0,
                "cancelled": 0,
            },
            "status": "active",
        }

        self.vector_stores[vector_store_id] = vector_store
        return vector_store

    def get_vector_store(self, vector_store_id: str):
        """Get a specific vector store"""
        if vector_store_id not in self.vector_stores:
            raise HTTPException(status_code=404, detail="Vector store not found")
        return self.vector_stores[vector_store_id]

    def modify_vector_store(
        self,
        vector_store_id: str,
        name: str | None = None,
        metadata: dict | None = None,
    ):
        """Modify a vector store"""
        if vector_store_id not in self.vector_stores:
            raise HTTPException(status_code=404, detail="Vector store not found")

        store = self.vector_stores[vector_store_id]
        if name is not None:
            store["name"] = name
        if metadata is not None:
            store["metadata"] = metadata

        return store

    def delete_vector_store(self, vector_store_id: str):
        """Delete a vector store"""
        if vector_store_id not in self.vector_stores:
            raise HTTPException(status_code=404, detail="Vector store not found")

        del self.vector_stores[vector_store_id]
        return {
            "id": vector_store_id,
            "object": "vector_store.deleted",
            "deleted": True,
        }

    def create_vector_store_file_batch(self, vector_store_id: str, file_ids: list[str]):
        """Create a batch for processing files in a vector store"""
        if vector_store_id not in self.vector_stores:
            raise HTTPException(status_code=404, detail="Vector store not found")

        batch_id = f"batch_{uuid.uuid4().hex}"

        batch = {
            "id": batch_id,
            "object": "vector_store.file_batch",
            "vector_store_id": vector_store_id,
            "file_ids": file_ids,
            "created_at": datetime.utcnow().isoformat(),
            "status": "in_progress",
        }

        # Store batch information
        if "batches" not in self.vector_stores[vector_store_id]:
            self.vector_stores[vector_store_id]["batches"] = {}
        self.vector_stores[vector_store_id]["batches"][batch_id] = batch

        return batch

    def get_vector_store_file_batch(self, vector_store_id: str, batch_id: str):
        """Get a specific file batch"""
        if vector_store_id not in self.vector_stores:
            raise HTTPException(status_code=404, detail="Vector store not found")

        store = self.vector_stores[vector_store_id]
        if "batches" not in store or batch_id not in store["batches"]:
            raise HTTPException(status_code=404, detail="File batch not found")

        return store["batches"][batch_id]

    def cancel_vector_store_file_batch(self, vector_store_id: str, batch_id: str):
        """Cancel a file batch"""
        batch = self.get_vector_store_file_batch(vector_store_id, batch_id)
        batch["status"] = "cancelled"
        return batch

    def list_files_in_vector_store_batch(
        self,
        vector_store_id: str,
        batch_id: str,
        limit: int = 20,
        order: str = "desc",
        after: str | None = None,
        before: str | None = None,
        filter: str | None = None,
    ):
        """List files in a specific batch"""
        batch = self.get_vector_store_file_batch(vector_store_id, batch_id)

        # This would typically return file objects, but for now we'll return the file IDs
        files = [
            {"id": file_id, "object": "vector_store.file"}
            for file_id in batch["file_ids"]
        ]

        return {
            "object": "list",
            "data": files,
            "first_id": files[0]["id"] if files else None,
            "last_id": files[-1]["id"] if files else None,
            "has_more": False,
        }

    def list_vector_store_files(
        self,
        vector_store_id: str,
        limit: int = 20,
        order: str = "desc",
        after: str | None = None,
        before: str | None = None,
        filter: str | None = None,
    ):
        """List all files in a vector store"""
        if vector_store_id not in self.vector_stores:
            raise HTTPException(status_code=404, detail="Vector store not found")

        # This would typically return actual file objects
        # For now, return a placeholder
        return {
            "object": "list",
            "data": [],
            "first_id": None,
            "last_id": None,
            "has_more": False,
        }

    def create_vector_store_file(self, vector_store_id: str, file_id: str):
        """Create a file in a vector store"""
        if vector_store_id not in self.vector_stores:
            raise HTTPException(status_code=404, detail="Vector store not found")

        file_obj = {
            "id": file_id,
            "object": "vector_store.file",
            "vector_store_id": vector_store_id,
            "created_at": datetime.utcnow().isoformat(),
            "status": "completed",
        }

        return file_obj

    def get_vector_store_file(self, vector_store_id: str, file_id: str):
        """Get a specific file in a vector store"""
        if vector_store_id not in self.vector_stores:
            raise HTTPException(status_code=404, detail="Vector store not found")

        # This would typically return the actual file object
        # For now, return a placeholder
        return {
            "id": file_id,
            "object": "vector_store.file",
            "vector_store_id": vector_store_id,
            "created_at": datetime.utcnow().isoformat(),
            "status": "completed",
        }

    def delete_vector_store_file(self, vector_store_id: str, file_id: str):
        """Delete a file from a vector store"""
        if vector_store_id not in self.vector_stores:
            raise HTTPException(status_code=404, detail="Vector store not found")

        return {"id": file_id, "object": "vector_store.file.deleted", "deleted": True}

    def update_vector_store_file_attributes(
        self, vector_store_id: str, file_id: str, metadata: dict | None = None
    ):
        """Update file attributes"""
        file_obj = self.get_vector_store_file(vector_store_id, file_id)
        if metadata is not None:
            file_obj["metadata"] = metadata
        return file_obj

    def retrieve_vector_store_file_content(self, vector_store_id: str, file_id: str):
        """Retrieve file content from a vector store"""
        if vector_store_id not in self.vector_stores:
            raise HTTPException(status_code=404, detail="Vector store not found")

        # This would typically return the actual file content
        # For now, return a placeholder
        return {
            "id": file_id,
            "object": "vector_store.file.content",
            "content": "File content placeholder",
        }

    def search_vector_store(self, vector_store_id: str, query: str, k: int = 10):
        """Search a vector store"""
        if vector_store_id not in self.vector_stores:
            raise HTTPException(status_code=404, detail="Vector store not found")

        # This would typically use the actual vector store instance
        # For now, return a placeholder
        return {
            "object": "list",
            "data": [],
            "first_id": None,
            "last_id": None,
            "has_more": False,
        }
