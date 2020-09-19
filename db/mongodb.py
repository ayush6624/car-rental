from motor.motor_asyncio import AsyncIOMotorClient
from utils.config import MONGODB_URL, MAX_CONNECTIONS_COUNT, MIN_CONNECTIONS_COUNT
from models.user import UserInDB
from src import app
from typing import Optional


class MongoDB:
    client: AsyncIOMotorClient = None


db = MongoDB()


@app.on_event("startup")
async def connect_to_mongo():
    db.client = AsyncIOMotorClient(MONGODB_URL)
    print("MongoDB Connected")


@app.on_event("shutdown")
async def close_mongo_connection():
    db.client.close()
    print("MongoDB Disconnected")


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


async def get_locations(city: Optional[str] = None):
    client = await get_nosql_db()
    db = client["car_rental"]
    collection = db.locations
    if city:
        row = collection.find({"city_link_name": city})
    else:
        row = collection.find({})
    row = await row.to_list(length=100)
    for i in row:
        i['_id'] = str(i['_id'])
    return {"locations": row}


async def get_cars():
    client = await get_nosql_db()
    db = client["car_rental"]
    collection = db.cars
    row = collection.find({})
    row = await row.to_list(length=100)
    for i in row:
        i['_id'] = str(i['_id'])
    return {"cars": row}
