from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient

from .config import settings

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello world"}


@app.get("/health-check/mongodb")
async def health_check_mongodb():
    client = AsyncIOMotorClient(settings.uri)
    try:
        await client.admin.command("ping")
        return {
            "message": "Pinged your deployment. You have successfully connected to MongoDB!"
        }
    except Exception as e:
        return {"message": str(e)}


@app.get("/info")
async def info():
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user,
    }
