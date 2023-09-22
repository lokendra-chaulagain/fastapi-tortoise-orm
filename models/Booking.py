from tortoise import fields
from tortoise.models import Model



BOOKING_STATUS = (
    ('Used', 'Used'),
    ('Used Partially', 'Used Partially'),
    ('Unused', 'Unused'),
    ('Cancelled', 'Cancelled')
)


class Booking(Model):
    id = fields.IntField(pk=True)
    guest = fields.ForeignKeyField(
        "models.Guest", related_name='bookings', on_delete=fields.CASCADE)
    room = fields.ForeignKeyField(
        "models.Room", related_name='bookings', on_delete=fields.CASCADE)
    from_date = fields.DateField()
    to_date = fields.DateField()
    status = fields.CharField(
        max_length=20, choices=BOOKING_STATUS, default='Unused')
    advance_amount = fields.FloatField(default=0)
