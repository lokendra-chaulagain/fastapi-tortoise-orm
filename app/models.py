from tortoise import fields ,Tortoise 
from tortoise.models import Model
from pydantic import BaseModel
from tortoise.contrib.fastapi import register_tortoise


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    email = fields.CharField(max_length=255)


class UserIn(BaseModel):
    name: str
    email: str


class UserOut(BaseModel):
    id: int
    name: str
    email: str


TORTOISE_ORM = {
    "connections": {"default": "postgres://fnrlflit:APSQdQS6WBhMsxkC7nF4GrBfFI64tBs0@berry.db.elephantsql.com/fnrlflit"},  # Replace with your database connection string
    "apps": {
        "models": ["__main__"],  # Point to the module where your models are defined
        "default_connection": "default",
    },
}

def init_db(app):
    Tortoise.init(config=TORTOISE_ORM)
    Tortoise.generate_schemas()
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=True,
        add_exception_handlers=True,
    )