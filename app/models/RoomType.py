from tortoise import fields, Tortoise
from tortoise.models import Model
from pydantic import BaseModel
from tortoise.contrib.fastapi import register_tortoise


class RoomType(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    rate = fields.IntField()
