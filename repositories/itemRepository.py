from typing import List
from schemas.itemSchems import ItemIn, ItemOut, ItemQueryParams
from models.Item import Item
from fastapi import HTTPException


async def itemRepository_get_all(query_params: ItemQueryParams) -> List[ItemOut]:
    offset = (query_params.page - 1) * query_params.limit
    query = Item.all()

    if query_params.name:
        query = query.filter(name__icontains=query_params.name)

    items = await query.offset(offset).limit(query_params.limit)
    return list(items)


async def itemRepository_create(item: ItemIn) -> ItemOut:
    item = await Item.create(**item.model_dump())
    return item


async def itemRepository_update(item_id: int, updated_item: ItemIn) -> ItemOut:
    item = await Item.get_or_none(id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    item.name = updated_item.name
    await item.save()
    return item


async def itemRepository_get_one(item_id: int) -> ItemOut:
    item = await Item.get_or_none(id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


async def itemRepository_delete(item_id: int) -> ItemOut:
    item = await Item.get_or_none(id=item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    await item.delete()
    return item
