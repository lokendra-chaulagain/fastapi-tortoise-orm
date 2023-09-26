

from typing import List
from schemas.itemSchems import ItemIn, ItemOut, ItemQueryParams
from repositories.itemRepository import itemRepository_get_all, itemRepository_create, itemRepository_get_one, itemRepository_delete, itemRepository_update


async def itemService_get_all(query_params: ItemQueryParams) -> List[ItemOut]:
    return await itemRepository_get_all(query_params)


async def itemService_create(item: ItemIn) -> ItemOut:
    return await itemRepository_create(item)


async def itemService_get_one(item_id: int) -> ItemOut:
    return await itemRepository_get_one(item_id)


async def itemService_delete(item_id: int) -> ItemOut:
    return await itemRepository_delete(item_id)


async def itemService_update(item_id: int, updated_item: ItemIn) -> ItemOut:
    return await itemRepository_update(item_id, updated_item)
