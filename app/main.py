from fastapi import FastAPI

from .config import settings
from .database import client
from .routers import router_students

app = FastAPI(
    title="Student Course API",
    summary="A sample application showing how to use FastAPI to add a ReST API to a MongoDB collection.",
)


@app.get("/")
def root():
    return {"message": "Hello world"}


@app.get("/health-check/mongodb")
async def health_check_mongodb():
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

app.include_router(router_students.router)
