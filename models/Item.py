from tortoise import fields
from tortoise.models import Model


class Item(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=200)
    item_unit = fields.ManyToManyRelation(
        "models.ItemUnit", related_name='items', on_delete=fields.CASCADE)
    is_inventory_trackable = fields.BooleanField(default=False)
    is_service_item = fields.BooleanField(default=False)
    # category = TreeForeignKey(ItemCategory, related_name="items", on_delete=fields.CASCADE)
