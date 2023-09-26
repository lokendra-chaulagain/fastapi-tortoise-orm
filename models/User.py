from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    fullName = fields.CharField(max_length=225)
    email = fields.CharField(max_length=225)
    password = fields.CharField(max_length=225)
