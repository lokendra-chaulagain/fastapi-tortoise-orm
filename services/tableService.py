

from typing import List
from schemas.tableSchema import TableIn, TableOut, TableQueryParams
from repositories.tableRepository import tableRepository_get_all, tableRepository_create, tableRepository_get_one, tableRepository_delete, tableRepository_update


async def tableService_get_all(query_params: TableQueryParams) -> List[TableOut]:
    return await tableRepository_get_all(query_params)


async def tableService_create(table: TableIn) -> TableOut:
    return await tableRepository_create(table)


async def tableService_get_one(table_id: int) -> TableOut:
    return await tableRepository_get_one(table_id)


async def tableService_delete(table_id: int) -> TableOut:
    return await tableRepository_delete(table_id)


async def tableService_update(table_id: int, updated_table: TableIn) -> TableOut:
    return await tableRepository_update(table_id, updated_table)
