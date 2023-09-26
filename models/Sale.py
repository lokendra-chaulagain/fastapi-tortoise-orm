from tortoise import fields
from tortoise.models import Model


class Sale(Model):  # bill
    id = fields.IntField(pk=True)
    discount_amount = fields.FloatField(default=0)
    is_draft = fields.BooleanField(default=True)
    table = fields.ForeignKeyField(
        "models.Table", related_name='sales', on_delete=fields.NO_ACTION)
