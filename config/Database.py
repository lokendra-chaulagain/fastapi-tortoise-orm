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
            "models": ["models.RoomType", "models.Room", "models.Guest", "models.Booking", "models.CheckIn", "models.CheckInGuestDetail", "models.Item", "models.ItemUnit", "models.User", "models.Party", "models.Table", "models.Order", "models.PurchaseRow", "models.Purchase", "models.Sale", "models.Table", "models.InventoryAccount", "models.InventoryAccount", "models.ItemCategory", "aerich.models"],
            "default_connection": "default",
        },
    }
}
