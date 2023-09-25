from tortoise import fields
from tortoise.models import Model


class Sale(Model):
    id = fields.IntField(pk=True)
    order = fields.ManyToManyField("models.Order", related_name='sales')
    discount_amount = fields.FloatField(default=0)
    timestamp = fields.DatetimeField(auto_now_add=True)
    # staff = fields.ForeignKeyField(
    #     "models.User", related_name='approved_sales', on_delete=fields.NO_ACTION)
    # check_in = fields.ForeignKeyField(
    #     "models.CheckIn", related_name='sales', on_delete=fields.CASCADE, null=True, blank=True)
