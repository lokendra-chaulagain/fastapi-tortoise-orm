from typing import Optional
from pydantic import BaseModel


class TokenDataIn(BaseModel):
    email: str
