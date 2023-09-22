from tortoise import fields
from tortoise.models import Model


class ItemCategory(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)
    description = fields.TextField(max_length=254, null=True, blank=True)
    # parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
