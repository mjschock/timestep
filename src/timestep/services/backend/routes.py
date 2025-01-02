from typing import List

from fastapi import APIRouter, HTTPException
from models import Item, ItemCreate

router = APIRouter()

# Simulate a database
items_db: List[Item] = []
current_id = 1


@router.get("/items", response_model=List[Item])
async def get_items():
    return items_db


@router.post("/items", response_model=Item)
async def create_item(item: ItemCreate):
    global current_id
    new_item = Item(id=current_id, **item.dict())
    items_db.append(new_item)
    current_id += 1
    return new_item


@router.delete("/items/{item_id}")
async def delete_item(item_id: int):
    for idx, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(idx)
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
