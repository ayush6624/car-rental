from models.user import UserInDB
from db.mongodb import get_nosql_db
from fastapi import Depends, HTTPException, status
from utils.config import MONGODB_URL, SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from jose import JWTError, jwt
from models.user import TokenData
from .auth import oauth2_scheme


async def get_user(name) -> UserInDB:
    client = await get_nosql_db()
    db = client["car_rental"]
    collection = db.users
    row = await collection.find_one({"username": name})
    if row is not None:
        return UserInDB(**row)
    else:
        return None


async def get_current_user(token: str = Depends(oauth2_scheme)):
    print('get_current_usr')
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = await get_user(token_data.username)
    if user is None:
        raise credentials_exception
    return user
