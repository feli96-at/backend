from typing import List, Optional

from bson import ObjectId
from pydantic import BaseModel, ConfigDict, Field

from ..database import PyObjectId, db

user_collection = db.get_collection("users")


class UserModel(BaseModel):
    id: PyObjectId = Field(alias="_id")
    name: str
    username: str
    password: str


class RegisterUserModel(BaseModel):
    name: str = Field(...)
    username: str = Field(...)
    password: str = Field(...)


class UserResponseModel(BaseModel):
    id: PyObjectId = Field(alias="_id", default="string")
    name: str = "string"
    username: str = "string"
