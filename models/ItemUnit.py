from tortoise import fields
from tortoise.models import Model


class ItemUnit(Model):
    id = fields.IntField(pk=True)
    unit_name = fields.CharField(max_length=50)
    item = fields.ManyToManyRelation(
        "models.Item", related_name='units', on_delete=fields.CASCADE)
    selling_price = fields.FloatField(null=True, blank=True)
    ratio = fields.FloatField(default=1)
