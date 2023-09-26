
from fastapi import FastAPI
from tortoise import Tortoise
from routes.tableRoute import tableRouter
from routes.saleRoute import saleRouter
# from routes.itemRoute import itemRouter
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
app.include_router(tableRouter, prefix="/tables", tags=["tables"])
app.include_router(saleRouter, prefix="/sales", tags=["sales"])
# app.include_router(itemRouter, prefix="/items", tags=["items"])
