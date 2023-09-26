from fastapi import APIRouter
from schemas.authSchema import LoginIn, LoginOut, RegisterIn, RegisterOut, UserFromTokenOut
from services.authService import authService_register, authService_login, authService_get_user_from_token
authRouter = APIRouter()


@authRouter.post("/register", response_model=RegisterOut)
async def user_register(user: RegisterIn):
    return await authService_register(user)


@authRouter.post("/login", response_model=LoginOut)
async def user_login(user: LoginIn):
    return await authService_login(user)


@authRouter.get("/get-user-from-token", response_model=UserFromTokenOut)
async def get_user_from_token(token: str):
    return await authService_get_user_from_token(token)
