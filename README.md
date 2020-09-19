# Car-Rental

## To-Do

- [ ] Convert User signup functions into class based functions
- [ ] Deployment
  - [ ] Docker
  - [ ] GCP Cloud Run
- [ ] Cart
- [ ] Promocode
- [ ] Frontend
  - [ ] call by location name

https://fastapi.tiangolo.com/advanced/nosql-databases/#define-a-constant-to-use-as-a-document-type
Cities - https://api.zoomcar.com/v4/cities?platform=web
Airport - https://api.zoomcar.com/v4/airport_terminals?platform=web

## Run

> uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload
> localhost:8000/docs

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

# Cars

https://api.zoomcar.com/v4/search?lat=28.554621&lng=77.088118&starts=2020-09-20%2012%3A30&ends=2020-09-21%2018%3A30&type=zoom_air&terminal_id=3&bracket=no_fuel&platform=web&version=2&device_id=000&device_name=000&city=delhi&zap=true
