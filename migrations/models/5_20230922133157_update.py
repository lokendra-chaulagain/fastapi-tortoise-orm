from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "booking" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "from_date" DATE NOT NULL,
    "to_date" DATE NOT NULL,
    "status" VARCHAR(20) NOT NULL  DEFAULT 'Unused',
    "advance_amount" DOUBLE PRECISION NOT NULL  DEFAULT 0,
    "guest_id" INT NOT NULL REFERENCES "guest" ("id") ON DELETE CASCADE,
    "room_id" INT NOT NULL REFERENCES "room" ("id") ON DELETE CASCADE
);
        CREATE TABLE IF NOT EXISTS "checkin" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "check_in_datetime" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "check_out_datetime" TIMESTAMPTZ,
    "is_booked_checkin" BOOL NOT NULL  DEFAULT False,
    "advance_amount" DOUBLE PRECISION NOT NULL  DEFAULT 0,
    "room_rate" DOUBLE PRECISION,
    "guest_id" INT NOT NULL REFERENCES "guest" ("id") ON DELETE CASCADE,
    "room_id" INT NOT NULL REFERENCES "room" ("id") ON DELETE CASCADE,
    "booking_id" INT  UNIQUE REFERENCES "booking" ("id") ON DELETE CASCADE
);
        CREATE TABLE IF NOT EXISTS "checkinguestdetail" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "full_name" VARCHAR(250) NOT NULL,
    "nationality" VARCHAR(150) NOT NULL,
    "no_of_person" INT NOT NULL,
    "sex" VARCHAR(20) NOT NULL,
    "relation" VARCHAR(150) NOT NULL,
    "profession" VARCHAR(150) NOT NULL,
    "purpose_of_visit" VARCHAR(150) NOT NULL,
    "date_of_birth" DATE NOT NULL,
    "passport_number" VARCHAR(100)
);
        CREATE TABLE IF NOT EXISTS "item" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(200) NOT NULL,
    "is_inventory_trackable" BOOL NOT NULL  DEFAULT False,
    "is_service_item" BOOL NOT NULL  DEFAULT False
);
        CREATE TABLE IF NOT EXISTS "itemunit" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "unit_name" VARCHAR(50) NOT NULL,
    "selling_price" DOUBLE PRECISION,
    "ratio" DOUBLE PRECISION NOT NULL  DEFAULT 1,
    "item_id" INT NOT NULL REFERENCES "item" ("id") ON DELETE CASCADE
);
        CREATE TABLE IF NOT EXISTS "user" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "full_name" VARCHAR(245) NOT NULL,
    "email" VARCHAR(254) NOT NULL UNIQUE,
    "is_active" BOOL NOT NULL  DEFAULT True,
    "is_staff" BOOL NOT NULL  DEFAULT False,
    "is_superuser" BOOL NOT NULL  DEFAULT False
);
        CREATE TABLE IF NOT EXISTS "party" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "room_id" INT REFERENCES "room" ("id") ON DELETE CASCADE,
    "table_id" INT REFERENCES "table" ("id") ON DELETE CASCADE
);
        CREATE TABLE IF NOT EXISTS "table" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(20) NOT NULL
);
        CREATE TABLE IF NOT EXISTS "order" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "quantity" DOUBLE PRECISION NOT NULL,
    "rate" DOUBLE PRECISION NOT NULL,
    "amount" DOUBLE PRECISION NOT NULL,
    "status" VARCHAR(50) NOT NULL  DEFAULT 'Unpaid',
    "timestamp" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "item_id" INT NOT NULL REFERENCES "item" ("id") ON DELETE CASCADE,
    "party_id" INT NOT NULL REFERENCES "party" ("id") ON DELETE NO ACTION,
    "staff_id" INT REFERENCES "user" ("id") ON DELETE NO ACTION,
    "unit_id" INT REFERENCES "itemunit" ("id") ON DELETE NO ACTION
);
        CREATE TABLE IF NOT EXISTS "purchaserow" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "quantity" DOUBLE PRECISION NOT NULL,
    "rate" DOUBLE PRECISION NOT NULL,
    "total_amount" DOUBLE PRECISION NOT NULL,
    "timestamp" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "status" VARCHAR(50) NOT NULL  DEFAULT 'Not Committed Purchase',
    "item_id" INT NOT NULL REFERENCES "item" ("id") ON DELETE NO ACTION,
    "staff_id" INT REFERENCES "user" ("id") ON DELETE NO ACTION,
    "unit_id" INT REFERENCES "itemunit" ("id") ON DELETE NO ACTION
);
        CREATE TABLE IF NOT EXISTS "purchase" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "timestamp" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "staff_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE NO ACTION
);
        CREATE TABLE IF NOT EXISTS "sale" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "timestamp" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "discount_amount" DOUBLE PRECISION NOT NULL  DEFAULT 0,
    "check_in_id" INT REFERENCES "checkin" ("id") ON DELETE CASCADE,
    "staff_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE NO ACTION
);
        CREATE TABLE IF NOT EXISTS "inventoryaccount" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "debit" DOUBLE PRECISION NOT NULL  DEFAULT 0,
    "credit" DOUBLE PRECISION NOT NULL  DEFAULT 0,
    "timestamp" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "bill_id" INT NOT NULL,
    "item_id" INT NOT NULL REFERENCES "item" ("id") ON DELETE NO ACTION
);
        CREATE TABLE IF NOT EXISTS "itemcategory" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL,
    "description" TEXT
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "booking";
        DROP TABLE IF EXISTS "checkin";
        DROP TABLE IF EXISTS "checkinguestdetail";
        DROP TABLE IF EXISTS "item";
        DROP TABLE IF EXISTS "itemunit";
        DROP TABLE IF EXISTS "user";
        DROP TABLE IF EXISTS "party";
        DROP TABLE IF EXISTS "table";
        DROP TABLE IF EXISTS "order";
        DROP TABLE IF EXISTS "purchaserow";
        DROP TABLE IF EXISTS "purchase";
        DROP TABLE IF EXISTS "sale";
        DROP TABLE IF EXISTS "inventoryaccount";
        DROP TABLE IF EXISTS "itemcategory";"""
