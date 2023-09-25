from typing import Optional
from pydantic import BaseModel, ValidationError


class GuestIn(BaseModel):
    name: str
    address: str
    phone: str
    email: str
    citizenship_no: str
    complete: bool


class GuestOut(BaseModel):
    id: int
    name: str
    address: str
    phone: str
    email: str
    citizenship_no: str
    complete: bool


class GuestQueryParams(BaseModel):
    page: Optional[int] = 1
    limit: Optional[int] = 5
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
