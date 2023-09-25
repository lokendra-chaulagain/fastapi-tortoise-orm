from tortoise import fields
from tortoise.models import Model


class RoomType(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    rate = fields.IntField()
