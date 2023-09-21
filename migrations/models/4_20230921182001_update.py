from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "room" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "no" INT NOT NULL UNIQUE,
    "suspended" BOOL NOT NULL  DEFAULT False,
    "capacity" INT NOT NULL,
    "rate" INT NOT NULL,
    "type_id" INT NOT NULL REFERENCES "roomtype" ("id") ON DELETE CASCADE
);
        CREATE TABLE IF NOT EXISTS "guest" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(150) NOT NULL,
    "address" VARCHAR(250) NOT NULL,
    "phone" VARCHAR(13) NOT NULL,
    "email" VARCHAR(25),
    "citizenship_no" VARCHAR(50),
    "complete" BOOL NOT NULL  DEFAULT False
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "room";
        DROP TABLE IF EXISTS "guest";"""
