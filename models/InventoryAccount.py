from tortoise import fields
from tortoise.models import Model



class InventoryAccount(Model):
    id = fields.IntField(pk=True)
    item = fields.ForeignKeyField(
        "models.Item", related_name='inventory_accounts', on_delete=fields.NO_ACTION)
    debit = fields.FloatField(default=0.0)
    credit = fields.FloatField(default=0.0)
    timestamp = fields.DatetimeField(auto_now_add=True)
    # bill_type = fields.ForeignKey(ContentType, limit_choices_to={'name__in': ('sale', 'purchase',)},
    #                               on_delete=fields.CASCADE)
    bill_id = fields.IntField()
    # bill_object = GenericForeignKey('bill_type', 'bill_id')
