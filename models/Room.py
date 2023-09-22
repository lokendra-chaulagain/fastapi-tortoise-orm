from tortoise import fields, Tortoise
from tortoise.models import Model
from pydantic import BaseModel
from tortoise.contrib.fastapi import register_tortoise


class Room(Model):
    id = fields.IntField(pk=True)
    no = fields.IntField(unique=True)
    type = fields.ForeignKeyField(
        'models.RoomType', related_name='rooms', on_delete=fields.CASCADE)
    suspended = fields.BooleanField(default=False)
    capacity = fields.IntField()
    rate = fields.IntField()
