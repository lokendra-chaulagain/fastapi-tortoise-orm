from typing import List
from schemas.saleSchema import SaleIn, SaleOut, SaleQueryParams
from models.Sale import Sale
from fastapi import HTTPException


async def saleRepository_get_all(query_params: SaleQueryParams) -> List[SaleOut]:
    offset = (query_params.page - 1) * query_params.limit
    query = Sale.all()

    if query_params.table:
        query = query.filter(table__icontains=query_params.table)

    sales = await query.offset(offset).limit(query_params.limit)
    return list(sales)


async def saleRepository_create(sale: SaleIn) -> SaleOut:
    print(sale, "_____________________________________________________________________")
    # Table = {
    #     "id": 1,
    #     "name": "string1"
    # }
    # new_sale = await Sale.create(discount_amount=sale.discount_amount, is_draft=sale.is_draft, table=Table)
    # await new_sale.save()
    return {
        "id": 1,
        "discount_amount": 10,
        "is_draft": True,
        "table": 1 
    }


# async def saleRepository_create(sale: SaleIn) -> SaleOut:
#     # sale_data = sale.model_dump()  # Assuming this method returns a valid dictionary
#     # sale = await Sale.create(**sale_data)
#     # return sale
#     print(sale)
#     instance = await Sale.create(**sale.dict())
#     return instance


async def saleRepository_update(sale_id: int, updated_sale: SaleIn) -> SaleOut:
    sale = await Sale.get_or_none(id=sale_id)
    if sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    sale.name = updated_sale.name
    await sale.save()
    return sale


async def saleRepository_get_one(sale_id: int) -> SaleOut:
    sale = await Sale.get_or_none(id=sale_id)
    if sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale


async def saleRepository_delete(sale_id: int) -> SaleOut:
    sale = await Sale.get_or_none(id=sale_id)
    if sale is None:
        raise HTTPException(status_code=404, detail="Sale not found")
    await sale.delete()
    return sale
