from tortoise import fields
from tortoise.models import Model



class ItemUnit(Model):
    id = fields.IntField(pk=True)
    item = fields.ForeignKeyField(
        "models.Item", related_name='units', on_delete=fields.CASCADE)
    unit_name = fields.CharField(max_length=50)
    selling_price = fields.FloatField(null=True, blank=True)
    ratio = fields.FloatField(default=1)
