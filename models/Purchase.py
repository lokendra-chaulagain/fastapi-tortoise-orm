from tortoise import fields
from tortoise.models import Model



class Purchase(Model):
    id = fields.IntField(pk=True)
    purchases = fields.ManyToManyField(
        "models.PurchaseRow", related_name='sales')
    staff = fields.ForeignKeyField(
        "models.User", related_name='approved_purchases', on_delete=fields.NO_ACTION)
    timestamp = fields.DatetimeField(auto_now_add=True)
