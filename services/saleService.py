

from typing import List
from schemas.saleSchema import SaleIn, SaleOut, SaleQueryParams
from repositories.saleRepository import saleRepository_get_all, saleRepository_create, saleRepository_get_one, saleRepository_delete, saleRepository_update


async def saleService_get_all(query_params: SaleQueryParams) -> List[SaleOut]:
    return await saleRepository_get_all(query_params)


async def saleService_create(sale: SaleIn) -> SaleOut:
    return await saleRepository_create(sale)


async def saleService_get_one(sale_id: int) -> SaleOut:
    return await saleRepository_get_one(sale_id)


async def saleService_delete(sale_id: int) -> SaleOut:
    return await saleRepository_delete(sale_id)


async def saleService_update(sale_id: int, updated_sale: SaleIn) -> SaleOut:
    return await saleRepository_update(sale_id, updated_sale)
