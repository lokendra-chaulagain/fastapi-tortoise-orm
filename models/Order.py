from tortoise import fields
from tortoise.models import Model


ORDER_STATUS = (
    ('Unpaid', 'Unpaid'),
    ('Paid', 'Paid'),
)


class Order(Model):
    id = fields.IntField(pk=True)
    party = fields.ForeignKeyField(
        "models.Party", related_name='orders', on_delete=fields.NO_ACTION)
    item = fields.ForeignKeyField(
        'models.Item', on_delete=fields.CASCADE, related_name='orders')
    quantity = fields.FloatField()
    unit = fields.ForeignKeyField(
        "models.ItemUnit", related_name='orders', on_delete=fields.NO_ACTION, null=True, blank=True)
    rate = fields.FloatField()
    amount = fields.FloatField()
    staff = fields.ForeignKeyField(
        "models.User", related_name='orders', on_delete=fields.NO_ACTION, null=True, blank=True)
    status = fields.CharField(
        max_length=50, choices=ORDER_STATUS, default='Unpaid')
    timestamp = fields.DatetimeField(auto_now_add=True)
