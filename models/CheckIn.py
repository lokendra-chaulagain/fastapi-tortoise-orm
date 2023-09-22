from tortoise import fields
from tortoise.models import Model



class CheckIn(Model):
    id = fields.IntField(pk=True)
    guest = fields.ForeignKeyField(
        "models.Guest", related_name='check_ins', on_delete=fields.CASCADE)
    check_in_datetime = fields.DatetimeField(auto_now_add=True)
    check_out_datetime = fields.DatetimeField(null=True, blank=True)
    room = fields.ForeignKeyField(
        "models.Room", related_name='check_ins', on_delete=fields.CASCADE)
    is_booked_checkin = fields.BooleanField(default=False)
    booking = fields.OneToOneField(
        "models.Booking", related_name='check_in', on_delete=fields.CASCADE, null=True, blank=True)
    advance_amount = fields.FloatField(default=0)
    room_rate = fields.FloatField(null=True, blank=True)
