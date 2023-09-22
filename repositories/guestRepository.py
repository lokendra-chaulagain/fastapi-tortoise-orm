from typing import List
from schemas.guestSchema import GuestIn, GuestOut
from models.Guest import Guest
from fastapi import HTTPException


async def guestRepository_get_all() -> List[GuestOut]:
    guests = await Guest.all()
    return guests


async def guestRepository_create(guest: GuestIn) -> GuestOut:
    guest = await Guest.create(**guest.model_dump())
    return guest


async def guestRepository_update(guest_id: int, updated_guest: GuestIn) -> GuestOut:
    guest = await Guest.get_or_none(id=guest_id)
    if guest is None:
        raise HTTPException(status_code=404, detail="Guest not found")
    guest.name = updated_guest.name
    guest.address = updated_guest.address
    guest.phone = updated_guest.phone
    guest.email = updated_guest.email
    guest.citizenship_no = updated_guest.citizenship_no
    guest.complete = updated_guest.complete
    await guest.save()
    return guest


async def guestRepository_get_one(guest_id: int) -> GuestOut:
    guest = await Guest.get_or_none(id=guest_id)
    if guest is None:
        raise HTTPException(status_code=404, detail="Guest not found")
    return guest


async def guestRepository_delete(guest_id: int) -> GuestOut:
    guest = await Guest.get_or_none(id=guest_id)
    if guest is None:
        raise HTTPException(status_code=404, detail="Guest not found")
    await guest.delete()
    return guest
