from tortoise import fields ,Tortoise 
from tortoise.models import Model
from pydantic import BaseModel
from tortoise.contrib.fastapi import register_tortoise


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)


class UserIn(BaseModel):
    name: str
    email: str


class UserOut(BaseModel):
    id: int
    name: str
    email: str



class Product(Model):
    id = fields.IntField(pk=True)
    product_name = fields.CharField(max_length=255)
    product_email = fields.CharField(max_length=255)