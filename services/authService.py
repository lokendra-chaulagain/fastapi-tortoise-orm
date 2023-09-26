

from repositories.authRepository import authRepository_register, authRepository_login, authRepository_get_user_from_token
from schemas.authSchema import UserFromTokenOut, LoginOut, RegisterOut, RegisterIn, LoginIn


async def authService_register(user: RegisterIn) -> RegisterOut:
    return await authRepository_register(user)


async def authService_login(user: LoginIn) -> LoginOut:
    return await authRepository_login(user)


async def authService_get_user_from_token(token: str) -> UserFromTokenOut:
    return await authRepository_get_user_from_token(token)
