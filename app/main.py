from fastapi import FastAPI
from tortoise import Tortoise
from services.guestService import guestRouter
app = FastAPI()


async def init():  # Initialize Tortoise ORM
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


TORTOISE_ORM = {
    "connections": {
        "default": "postgres://qbvzrnkt:dQXdInNZuNeIn99-l42kvdyIMljsp6yW@berry.db.elephantsql.com/qbvzrnkt"
    },
    "apps": {
        "models": {
            "models": ["models.RoomType", "models.Room", "models.Guest", "models.Booking", "models.CheckIn", "models.CheckInGuestDetail", "models.Item", "models.ItemUnit", "models.User", "models.Party", "models.Table", "models.Order", "models.PurchaseRow", "models.Purchase", "models.Sale", "models.Table", "models.InventoryAccount", "models.InventoryAccount", "models.ItemCategory", "aerich.models"],
            "default_connection": "default",
        },
    }
}


# Routes
app.include_router(guestRouter, prefix="/guests")
