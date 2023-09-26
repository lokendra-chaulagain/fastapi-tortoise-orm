

from typing import List
from schemas.userSchema import UserIn, UserOut, UserQueryParams
from repositories.userRepository import userRepository_get_all, userRepository_get_one, userRepository_delete, userRepository_update


async def userService_get_all(query_params: UserQueryParams) -> List[UserOut]:
    return await userRepository_get_all(query_params)


async def userService_get_one(user_id: int) -> UserOut:
    return await userRepository_get_one(user_id)


async def userService_delete(user_id: int) -> UserOut:
    return await userRepository_delete(user_id)


async def userService_update(user_id: int, updated_user: UserIn) -> UserOut:
    return await userRepository_update(user_id, updated_user)
