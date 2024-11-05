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
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Jane Doe",
                "username": "janedoe1122",
                "password": "123456",
            }
        },
    )


class UserResponseModel(BaseModel):
    id: PyObjectId = Field(alias="_id")
    name: str
    username: str
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "id": "5e1ac6b5c515c2a60f7e0ce8",
                "name": "Jane Doe",
                "username": "janedoe1122",
            }
        },
    )
