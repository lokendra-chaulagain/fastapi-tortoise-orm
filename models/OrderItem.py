# from tortoise import fields
# from tortoise.models import Model

# ORDER_STATUS = (
#     ('Ordered', 'Ordered'),
#     ('Preparing', 'Preparing'),
#     ('Prepared', 'Prepared'),
#     ('Served', 'Served'),
# )


# class OrderItem(Model):
#     id = fields.IntField(pk=True)
#     sale = fields.ForeignKeyField(
#         'models.Sale', related_name='order_items', on_delete=fields.CASCADE)
#     item = fields.ForeignKeyField(
#         'models.Item', related_name='order_items', on_delete=fields.CASCADE)
#     status = fields.CharField(choices=ORDER_STATUS, max_length=10)
#     rate = fields.FloatField()
#     amount = fields.FloatField()  # rate *quantity
#     quantity = fields.FloatField()  # make <=1
#     unit = fields.ForeignKeyField(
#         "models.ItemUnit", related_name='orders', on_delete=fields.NO_ACTION, null=True, blank=True)
#     timestamp = fields.DatetimeField(auto_now_add=True)
