

from typing import List
from schemas.guestSchema import GuestIn, GuestOut, GuestQueryParams
from repositories.guestRepository import guestRepository_get_all, guestRepository_create, guestRepository_get_one, guestRepository_delete, guestRepository_update


async def guestService_get_all(query_params: GuestQueryParams) -> List[GuestOut]:
    return await guestRepository_get_all(query_params)


async def guestService_create(guest: GuestIn) -> GuestOut:
    return await guestRepository_create(guest)


async def guestService_get_one(guest_id: int) -> GuestOut:
    return await guestRepository_get_one(guest_id)


async def guestService_delete(guest_id: int) -> GuestOut:
    return await guestRepository_delete(guest_id)


async def guestService_update(guest_id: int, updated_guest: GuestIn) -> GuestOut:
    return await guestRepository_update(guest_id, updated_guest)
