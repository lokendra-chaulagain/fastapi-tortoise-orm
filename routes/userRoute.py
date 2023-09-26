from fastapi import APIRouter, Depends
from typing import List
from schemas.userSchema import UserIn, UserOut, UserQueryParams
from services.userService import userService_get_all, userService_get_one, userService_delete, userService_update
userRouter = APIRouter()


@userRouter.get("", response_model=List[UserOut])
async def get_all_users(query_params: UserQueryParams = Depends()):
    return await userService_get_all(query_params)


@userRouter.put("", response_model=UserOut)
async def update_user(user_id: int, updated_user: UserIn):
    return await userService_update(user_id, updated_user)


@userRouter.get("/{user_id}", response_model=UserOut)
async def get_user(user_id: int):
    return await userService_get_one(user_id)


@userRouter.delete("/{user_id}", response_model=UserOut)
async def delete_user(user_id: int):
    return await userService_delete(user_id)
