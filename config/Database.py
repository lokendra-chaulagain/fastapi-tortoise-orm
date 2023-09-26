from tortoise import Tortoise
from .EnvironmentSettings import settings


async def init():  # Initialize Tortoise ORM
    await Tortoise.init(
        config=TORTOISE_ORM,
    )
    await Tortoise.generate_schemas()


TORTOISE_ORM = {
    "connections": {
        "default": settings.POSTGRES_DB_URL
    },
    "apps": {
        "models": {
            "models": ["models.Table", "models.Sale", "aerich.models"],
            "default_connection": "default",
        },
    }
}
