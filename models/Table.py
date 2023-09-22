from tortoise import fields
from tortoise.models import Model


class Table(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=20)
