from bson import ObjectId
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Address(BaseModel):
    pickup: str
    pickup_time: Optional[datetime] = None
    dropoff: Optional[str] = None
    dropoff_time: Optional[datetime] = None


class Cart(BaseModel):
    address: Address


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
    cart: Optional[Cart] = None


class UserInDB(User):
    hashed_password: str
    _id: ObjectId


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
