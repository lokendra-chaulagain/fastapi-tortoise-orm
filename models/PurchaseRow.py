from tortoise import fields
from tortoise.models import Model


PURCHASE_STATUS = (
    ('Committed Purchase', 'Committed Purchase'),
    ('Not Committed Purchase', 'Not Committed Purchase'),
)


class PurchaseRow(Model):
    id = fields.IntField(pk=True)
    item = fields.ForeignKeyField(
        "models.Item", related_name='purchase_rows', on_delete=fields.NO_ACTION)
    unit = fields.ForeignKeyField("models.ItemUnit", related_name='purchases_rows',
                                  on_delete=fields.NO_ACTION, null=True, blank=True)
    quantity = fields.FloatField()
    rate = fields.FloatField()
    total_amount = fields.FloatField()
    staff = fields.ForeignKeyField(
        "models.User", related_name='purchase_rows', on_delete=fields.NO_ACTION, null=True, blank=True)
    timestamp = fields.DatetimeField(auto_now_add=True)
    status = fields.CharField(
        max_length=50, choices=PURCHASE_STATUS, default='Not Committed Purchase')
