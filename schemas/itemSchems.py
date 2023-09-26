from typing import Optional
from pydantic import BaseModel, ValidationError


class ItemIn(BaseModel):
    name: str
    item_unit: int
    # is_inventory_trackable: bool
    is_service_item: bool
    is_test: bool


class ItemOut(BaseModel):
    id: int
    name: str
    item_unit: int
    # is_inventory_trackable: bool
    is_service_item: bool
    is_test: bool


class ItemQueryParams(BaseModel):
    page: Optional[int] = 1
    limit: Optional[int] = 5
    name: Optional[str] = None
