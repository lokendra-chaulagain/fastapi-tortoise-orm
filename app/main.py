from typing import List
from fastapi import FastAPI, HTTPException
from app.models import User, UserIn, UserOut
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()

@app.get("/users", response_model=List[UserOut])
async def get_users():
    users = await User.all()
    return users


@app.post("/users", response_model=UserOut)
async def create_user(user: UserIn):
    user_obj = await User.create(**user.model_dump())
    return user_obj


@app.put("/users/{user_id}", response_model=UserOut)
async def update_user(user_id: int, user_in: UserIn):
    user_obj = await User.get_or_none(id=user_id)
    if user_obj is None:
        raise HTTPException(status_code=404, detail="User not found")

    user_obj.name = user_in.name
    user_obj.email = user_in.email
    await user_obj.save()
    return user_obj


@app.get("/users/{user_id}", response_model=UserOut)
async def get_user(user_id: int):
    user_obj = await User.get_or_none(id=user_id)
    if user_obj is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user_obj


@app.delete("/users/{user_id}", response_model=UserOut)
async def delete_user(user_id: int):
    user_obj = await User.get_or_none(id=user_id)
    if user_obj is None:
        raise HTTPException(status_code=404, detail="User not found")
    await user_obj.delete()
    return user_obj


register_tortoise(
    app,
    # for now hardcoded
    db_url="postgres://fnrlflit:APSQdQS6WBhMsxkC7nF4GrBfFI64tBs0@berry.db.elephantsql.com/fnrlflit",
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
