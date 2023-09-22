from tortoise import fields
from tortoise.models import Model



class Party(Model):
    id = fields.IntField(pk=True)
    room = fields.ForeignKeyField(
        "models.Room", related_name='parties', on_delete=fields.CASCADE, null=True, blank=True)
    table = fields.ForeignKeyField(
        "models.Table", related_name='parties', on_delete=fields.CASCADE, null=True, blank=True)
