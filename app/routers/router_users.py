from bson import ObjectId
from fastapi import APIRouter, Body, HTTPException

from ..models import model_users

router = APIRouter(tags=["users"], prefix="/users")


@router.post(
    "/",
    response_model=model_users.UserResponseModel,
    status_code=201,
    response_model_by_alias=False,
)
async def register_user(register_user_model: model_users.RegisterUserModel = Body(...)):
    # if (
    #     await model_users.user_collection.find_one(
    #         {"username": register_user_model.username}
    #     )
    # ) is not None:
    #     raise HTTPException(
    #         status_code=400,
    #         detail=f"Username {register_user_model.username} already exists",
    #     )
    # new_user = await model_users.user_collection.insert_one(
    #     register_user_model.model_dump()
    # )
    # registered_user = await model_users.user_collection.find_one(
    #     {"_id": ObjectId(new_user.inserted_id)}
    # )
    # return registered_user
    return model_users.UserResponseModel()
