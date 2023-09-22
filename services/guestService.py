from fastapi import APIRouter, Depends, HTTPException
from typing import List
from schemas.guestSchema import GuestIn, GuestOut
from repositories.guestRepository import get_all, create_guest
guestRouter = APIRouter()


@guestRouter.get("", response_model=List[GuestOut])
async def get_guests():
    return await get_all()


@guestRouter.post("", response_model=GuestOut)
async def new_guest(guest: GuestIn):
    return await create_guest(guest)
