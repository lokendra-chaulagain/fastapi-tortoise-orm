from typing import List
from schemas.tableSchema import TableIn, TableOut, TableQueryParams
from models.Table import Table
from fastapi import HTTPException


async def tableRepository_get_all(query_params: TableQueryParams) -> List[TableOut]:
    offset = (query_params.page - 1) * query_params.limit
    query = Table.all()

    if query_params.name:
        query = query.filter(name__icontains=query_params.name)

    tables = await query.offset(offset).limit(query_params.limit)
    return list(tables)


async def tableRepository_create(table: TableIn) -> TableOut:
    table = await Table.create(**table.model_dump())
    return table


async def tableRepository_update(table_id: int, updated_table: TableIn) -> TableOut:
    table = await Table.get_or_none(id=table_id)
    if table is None:
        raise HTTPException(status_code=404, detail="Table not found")
    table.name = updated_table.name
    await table.save()
    return table


async def tableRepository_get_one(table_id: int) -> TableOut:
    table = await Table.get_or_none(id=table_id)
    if table is None:
        raise HTTPException(status_code=404, detail="Table not found")
    return table


async def tableRepository_delete(table_id: int) -> TableOut:
    table = await Table.get_or_none(id=table_id)
    if table is None:
        raise HTTPException(status_code=404, detail="Table not found")
    await table.delete()
    return table
