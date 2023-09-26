from typing import Optional
from pydantic import BaseModel


class LoginIn(BaseModel):
    email: str
    password: str


class LoginOut(BaseModel):
    # id: int
    fullName: str
    email: str
    access_token: str
    token_type: str


class RegisterIn(BaseModel):
    fullName: str
    email: str
    password: str


class RegisterOut(BaseModel):
    id: int
    fullName: str
    email: str
    # password: str


class UserFromTokenOut(BaseModel):
    id: int
    fullName: str
    email: str
