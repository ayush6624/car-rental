# Car-Rental

https://fastapi.tiangolo.com/
Login - https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/

https://fastapi.tiangolo.com/tutorial/security/

SQL - `sqlalchemy`
Mongo - `motor` 

https://motor.readthedocs.io/en/stable/
https://github.com/markqiu/fastapi-mongodb-realworld-example-app/tree/master/app

https://fastapi.tiangolo.com/advanced/nosql-databases/#define-a-constant-to-use-as-a-document-type

## Protected Route
@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}

    DATABASE_URL = "mongodb://localhost:27017"
client = motor.motor_asyncio.AsyncIOMotorClient(
    DATABASE_URL, uuidRepresentation="standard"
)
db = client["database_name"]
collection = db["users"]


app = FastAPI()


user_db = MongoDBUserDatabase(UserDB, collection)

https://frankie567.github.io/fastapi-users/configuration/databases/mongodb/

http://0.0.0.0:8000/docs