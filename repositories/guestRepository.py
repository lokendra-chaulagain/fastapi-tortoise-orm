from typing import List
from schemas.guestSchema import GuestIn, GuestOut
from models.Guest import Guest


async def get_all() -> List[GuestOut]:
    guests = await Guest.all()
    return guests


async def create_guest(guest: GuestIn):
    guest = await Guest.create(**guest.model_dump())
    return guest
