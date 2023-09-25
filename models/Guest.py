from tortoise import fields
from tortoise.models import Model


class Guest(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=150)
    address = fields.CharField(max_length=250)
    phone = fields.CharField(max_length=13)
    email = fields.CharField(null=True, blank=True, max_length=25)
    citizenship_no = fields.CharField(max_length=50, null=True, blank=True)
    complete = fields.BooleanField(default=False)
