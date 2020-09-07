from motor.motor_asyncio import AsyncIOMotorClient
import logging
from config import MONGODB_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT
from models.user import UserInDB

# MongoDB


class MongoDB:
    client: AsyncIOMotorClient = None


db = MongoDB()


async def get_nosql_db() -> AsyncIOMotorClient:
    return db.client


# async def create_user(request, collection):
#     salt = uuid.uuid4().hex
#     hashed_password = hashlib.sha512(request.password.encode(
#         "utf-8") + salt.encode("utf-8")).hexdigest()

#     user = {}
#     user["username"] = request.username
#     user["salt"] = salt
#     user["hashed_password"] = hashed_password
#     # user = User(**user)
#     dbuser = UserInDB(**user)
#     response = await collection.insert_one(dbuser.dict())
#     return {"id_inserted": str(response.inserted_id)}

async def get_user(name) -> UserInDB:
    client = await get_nosql_db()
    db = client["car_rental"]
    collection = db.users
    row = await collection.find_one({"username": name})
    if row is not None:
        return UserInDB(**row)
    else:
        return None


async def connect_to_mongo():
    db.client = AsyncIOMotorClient(
        str(MONGODB_URL), maxPoolSize=MAX_CONNECTIONS_COUNT, minPoolSize=MIN_CONNECTIONS_COUNT,
    )
    logging.info("connected to mongodb")


async def close_mongo_connection():
    db.client.close()
    logging.info("closed mongo connection")
