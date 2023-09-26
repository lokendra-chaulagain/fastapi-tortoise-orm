from typing import Optional
from pydantic import BaseModel


class UserIn(BaseModel):
    fullName: str
    email: str
    password: str


class UserOut(BaseModel):
    id: int
    fullName: str
    email: str
    # password: str


class UserQueryParams(BaseModel):
    page: Optional[int] = 1
    limit: Optional[int] = 5
    fullName: Optional[str] = None
    email: Optional[str] = None


# class UserLoginIn(BaseModel):
#     email: str
#     password: str


# class UserLoginResponse(BaseModel):
#     fullName: str
#     email: str
#     access_token: str
#     token_type: str
