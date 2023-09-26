from typing import Optional
from pydantic import BaseModel, ValidationError


class TableIn(BaseModel):
    name: str


class TableOut(BaseModel):
    id: int
    name: str


class TableQueryParams(BaseModel):
    page: Optional[int] = 1
    limit: Optional[int] = 5
    name: Optional[str] = None
