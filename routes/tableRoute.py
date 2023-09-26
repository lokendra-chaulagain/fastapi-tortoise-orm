from fastapi import APIRouter, Depends
from typing import List
from schemas.tableSchema import TableIn, TableOut, TableQueryParams
from services.tableService import tableService_get_all, tableService_create, tableService_get_one, tableService_delete, tableService_update
tableRouter = APIRouter()


@tableRouter.get("", response_model=List[TableOut])
async def get_all_tables(query_params: TableQueryParams = Depends()):
    return await tableService_get_all(query_params)


@tableRouter.post("", response_model=TableOut)
async def create_table(table: TableIn):
    return await tableService_create(table)


@tableRouter.put("", response_model=TableOut)
async def update_table(table_id: int, updated_table: TableIn):
    return await tableService_update(table_id, updated_table)


@tableRouter.get("/{table_id}", response_model=TableOut)
async def get_table(table_id: int):
    return await tableService_get_one(table_id)


@tableRouter.delete("/{table_id}", response_model=TableOut)
async def delete_table(table_id: int):
    return await tableService_delete(table_id)
