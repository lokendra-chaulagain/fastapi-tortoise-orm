
from fastapi import FastAPI
from tortoise import Tortoise
from routes.guestRoute import guestRouter
from config.Database import init
from config.EnvironmentSettings import settings

app = FastAPI(title=settings.APP_NAME, version=settings.API_VERSION)


@app.on_event("startup")
async def startup_db_client():
    await init()


@app.on_event("shutdown")
async def shutdown_db_client():
    await Tortoise.close_connections()


# Routes
app.include_router(guestRouter, prefix="/guests", tags=["guests"])
