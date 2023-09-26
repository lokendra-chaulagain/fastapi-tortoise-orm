from schemas.authSchema import UserFromTokenOut, RegisterIn, RegisterOut, LoginIn, LoginOut
from schemas.tokenSchema import TokenDataIn
from models.User import User
from fastapi import HTTPException, Depends, status
from jose import JWTError, jwt
from datetime import timedelta
from config.EnvironmentSettings import settings
from helpers.passwordHelper import get_password_hash, verify_password
from helpers.tokenHepler import create_access_token
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def authRepository_register(user: RegisterIn) -> RegisterOut:
    hashed_password = get_password_hash(user.password)
    new_user = await User.create(fullName=user.fullName, email=user.email, password=hashed_password)
    await new_user.save()
    return new_user


async def authRepository_login(user: LoginIn) -> LoginOut:
    existing_user = await User.get_or_none(email=user.email)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    password_match = verify_password(user.password, existing_user.password)

    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": existing_user.email}, expires_delta=access_token_expires)
    return {
        "fullName": existing_user.fullName,
        "email": existing_user.email,
        "access_token": access_token,
        "token_type": "bearer"
    }


async def authRepository_get_user_from_token(token: Annotated[str, Depends(oauth2_scheme)]) -> UserFromTokenOut:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY,
                             algorithms=[settings.JWT_ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenDataIn(email=email)
    except JWTError:
        raise credentials_exception
    user = await User.get_or_none(email=token_data.email)
    if user is None:
        raise credentials_exception

    return user
