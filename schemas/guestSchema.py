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
