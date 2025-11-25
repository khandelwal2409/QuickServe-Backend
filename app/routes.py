from fastapi import APIRouter, HTTPException
from typing import Dict
from .schemas import Item, ItemCreate

router = APIRouter(prefix="/api")

# In-memory fake DB
fake_db: Dict[int, Item] = {1: Item(id=1, name="Sample", description="A sample item")}


@router.get("/health")
async def health():
    return {"status": "ok"}


@router.get("/items/{item_id}", response_model=Item)
async def get_item(item_id: int):
    item = fake_db.get(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/items", response_model=Item, status_code=201)
async def create_item(payload: ItemCreate):
    new_id = max(fake_db.keys()) + 1 if fake_db else 1
    item = Item(id=new_id, **payload.dict())
    fake_db[new_id] = item
    return item
