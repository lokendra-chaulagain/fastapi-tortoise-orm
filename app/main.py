from typing import List
from fastapi import FastAPI, HTTPException
from app.models import User, UserIn, UserOut
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise

app = FastAPI()

# Initialize Tortoise ORM
async def init():
    await Tortoise.init(
        config=TORTOISE_ORM,
    )
    await Tortoise.generate_schemas()


@app.on_event("startup")
async def startup_db_client():
    await init()


@app.on_event("shutdown")
async def shutdown_db_client():
    await Tortoise.close_connections()


@app.get('/users', response_model=List[UserOut])
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


TORTOISE_ORM = {
    "connections": {
        "default": "postgres://qbvzrnkt:dQXdInNZuNeIn99-l42kvdyIMljsp6yW@berry.db.elephantsql.com/qbvzrnkt"
    },
    "apps": {
        "models": {
            "models": ["app.models", "aerich.models"],
            "default_connection": "default",
        },
    }
}


# register_tortoise(
#     app,
#     # for now hardcoded
#     db_url="postgres://fnrlflit:APSQdQS6WBhMsxkC7nF4GrBfFI64tBs0@berry.db.elephantsql.com/fnrlflit",
#     modules={"models": ["app.models"]},
#     generate_schemas=True,
#     add_exception_handlers=True,
# )


# TORTOISE_ORM = {
#     "connections": {"postgres://fnrlflit:APSQdQS6WBhMsxkC7nF4GrBfFI64tBs0@berry.db.elephantsql.com/fnrlflit"},
#     "apps": {
#         "models": {
#             "models": ["app.models", "aerich.models"],
#             "default_connection": "default",
#         },
#     },
# }
