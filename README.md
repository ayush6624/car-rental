# Car-Rental

## To-Do
- [ ] Convert User signup functions into class based functions
- [ ] Deployment
  - [ ] Docker
  - [ ] GCP Cloud Run
- [ ] Cart
- [ ] Promocode

https://fastapi.tiangolo.com/advanced/nosql-databases/#define-a-constant-to-use-as-a-document-type

Cities - https://api.zoomcar.com/v4/cities?platform=web
Airport - https://api.zoomcar.com/v4/airport_terminals?platform=web
## Run
> uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload

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


https://frankie567.github.io/fastapi-users/configuration/databases/mongodb/
http://0.0.0.0:8000/docs
http://0.0.0.0:8000/redoc


# Google Maps
https://maps.googleapis.com/maps/api/place/textsearch/json?query=Delhi&type=airport&key=AIzaSyAGNFsvRxrPWxm3at6ub4Ohjr98EqqTMUs
https://maps.googleapis.com/maps/api/place/textsearch/json?query=Delhi&type=train_station&key=AIzaSyAGNFsvRxrPWxm3at6ub4Ohjr98EqqTMUs

response.results[1].name