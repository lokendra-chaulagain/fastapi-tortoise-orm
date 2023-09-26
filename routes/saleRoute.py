from fastapi import APIRouter, Depends
from typing import List
from schemas.saleSchema import SaleIn, SaleOut, SaleQueryParams
from services.saleService import saleService_get_all, saleService_create, saleService_get_one, saleService_delete, saleService_update
saleRouter = APIRouter()


@saleRouter.get("", response_model=List[SaleOut])
async def get_all_sales(query_params: SaleQueryParams = Depends()):
    return await saleService_get_all(query_params)


@saleRouter.post("", response_model=SaleOut)
async def create_sale(sale: SaleIn):
    return await saleService_create(sale)


@saleRouter.put("", response_model=SaleOut)
async def update_sale(sale_id: int, updated_sale: SaleIn):
    return await saleService_update(sale_id, updated_sale)


@saleRouter.get("/{sale_id}", response_model=SaleOut)
async def get_sale(sale_id: int):
    return await saleService_get_one(sale_id)


@saleRouter.delete("/{sale_id}", response_model=SaleOut)
async def delete_sale(sale_id: int):
    return await saleService_delete(sale_id)
