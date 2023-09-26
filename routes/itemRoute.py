from fastapi import APIRouter, Depends
from typing import List
from schemas.itemSchems import ItemIn, ItemOut, ItemQueryParams
from services.itemService import itemService_get_all, itemService_create, itemService_get_one, itemService_delete, itemService_update
itemRouter = APIRouter()


@itemRouter.get("", response_model=List[ItemOut])
async def get_all_items(query_params: ItemQueryParams = Depends()):
    return await itemService_get_all(query_params)


@itemRouter.post("", response_model=ItemOut)
async def create_item(item: ItemIn):
    return await itemService_create(item)


@itemRouter.put("", response_model=ItemOut)
async def update_item(item_id: int, updated_item: ItemIn):
    return await itemService_update(item_id, updated_item)


@itemRouter.get("/{item_id}", response_model=ItemOut)
async def get_item(item_id: int):
    return await itemService_get_one(item_id)


@itemRouter.delete("/{item_id}", response_model=ItemOut)
async def delete_item(item_id: int):
    return await itemService_delete(item_id)
