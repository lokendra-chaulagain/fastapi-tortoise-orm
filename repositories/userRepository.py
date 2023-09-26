from typing import List, Annotated
from schemas.userSchema import UserIn, UserOut, UserQueryParams
from models.User import User
from fastapi import HTTPException, Depends, status
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
from datetime import datetime, timedelta
from config.EnvironmentSettings import settings


class TokenData(BaseModel):
    email: str | None = None


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


async def userRepository_get_all(query_params: UserQueryParams) -> List[UserOut]:
    offset = (query_params.page - 1) * query_params.limit
    query = User.all()

    if query_params.fullName:
        query = query.filter(fullName__icontains=query_params.fullName)
    if query_params.email:
        query = query.filter(email__icontains=query_params.email)

    users = await query.offset(offset).limit(query_params.limit)
    return list(users)


# async def userRepository_create(user: UserIn) -> UserOut:
#     hashed_password = get_password_hash(user.password)
#     new_user = await User.create(fullName=user.fullName, email=user.email, password=hashed_password)
#     await new_user.save()
#     return new_user


# async def userRepository_login(user: UserLoginIn) -> UserLoginResponse:
#     existing_user = await User.get_or_none(email=user.email)
#     if existing_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     password_match = verify_password(user.password, existing_user.password)

#     access_token_expires = timedelta(
#         minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": existing_user.email}, expires_delta=access_token_expires)
#     return {
#         "fullName": existing_user.fullName,
#         "email": existing_user.email,
#         "access_token": access_token,
#         "token_type": "bearer"
#     }


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return encoded_jwt


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> UserOut:
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
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    user = await User.get_or_none(email=token_data.email)
    if user is None:
        raise credentials_exception

    return user


async def userRepository_update(user_id: int, updated_user: UserIn) -> UserOut:
    user = await User.get_or_none(id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user.fullName = updated_user.fullName
    user.email = updated_user.email
    user.password = updated_user.password
    await user.save()
    return user


async def userRepository_get_one(user_id: int) -> UserOut:
    user = await User.get_or_none(id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


async def userRepository_delete(user_id: int) -> UserOut:
    user = await User.get_or_none(id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    await user.delete()
    return user
