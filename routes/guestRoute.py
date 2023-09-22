from fastapi import APIRouter
from typing import List
from schemas.guestSchema import GuestIn, GuestOut
from services.guestService import guestService_get_all, guestService_create, guestService_get_one, guestService_delete, guestService_update
guestRouter = APIRouter()


@guestRouter.get("", response_model=List[GuestOut])
async def get_all_guests():
    return await guestService_get_all()


@guestRouter.post("", response_model=GuestOut)
async def create_guest(guest: GuestIn):
    return await guestService_create(guest)


@guestRouter.put("", response_model=GuestOut)
async def update_guest(guest_id: int, updated_guest: GuestIn):
    return await guestService_update(guest_id, updated_guest)


@guestRouter.get("/{guest_id}", response_model=GuestOut)
async def get_guest(guest_id: int):
    return await guestService_get_one(guest_id)


@guestRouter.delete("/{guest_id}", response_model=GuestOut)
async def delete_guest(guest_id: int):
    return await guestService_delete(guest_id)
