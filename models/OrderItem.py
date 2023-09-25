from tortoise import fields
from tortoise.models import Model

ORDER_STATUS = (
    ('Ordered', 'Ordered'),
    ('Preparing', 'Preparing'),
    ('Prepared', 'Prepared'),
    ('Served', 'Served'),
)


class OrderItem(Model):
    id = fields.IntField(pk=True)
    sale = fields.ForeignKeyField(
        'models.Sale', related_name='order_items', on_delete=fields.CASCADE)
    item_unit = fields.ForeignKeyField(
        'models.ItemUnit', related_name='order_items', on_delete=fields.CASCADE)
    status = fields.CharField(choices=ORDER_STATUS, max_length=10)
