# Car-Rental

https://fastapi.tiangolo.com/
Login - https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/

https://fastapi.tiangolo.com/tutorial/security/



## Protected Route
@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}