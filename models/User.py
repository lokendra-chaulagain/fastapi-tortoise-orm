from tortoise import fields
from tortoise.models import Model


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    full_name = fields.CharField(max_length=245)
    email = fields.CharField(verbose_name='email address',
                             max_length=254, unique=True, db_index=True)
    is_active = fields.BooleanField(default=True)
    is_staff = fields.BooleanField(default=False)
    is_superuser = fields.BooleanField(default=False)
    # groups = fields.ManyToManyField(
    #     "models.Group", related_name='users', blank=True)
