from tortoise import fields
from tortoise.models import Model


SEX_CHOICE = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
)


class CheckInGuestDetail(Model):
    id = fields.IntField(pk=True)
    full_name = fields.CharField(max_length=250)
    nationality = fields.CharField(max_length=150)
    no_of_person = fields.IntField()
    sex = fields.CharField(choices=SEX_CHOICE, max_length=20)
    relation = fields.CharField(max_length=150)
    profession = fields.CharField(max_length=150)
    purpose_of_visit = fields.CharField(max_length=150)
    date_of_birth = fields.DateField()
    passport_number = fields.CharField(max_length=100, null=True, blank=True)
