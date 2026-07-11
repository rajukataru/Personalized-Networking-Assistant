from fastapi import FastAPI
from backend.database import engine, Base
from backend.routes import router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Personalized Networking Assistant",
    description="AI-powered networking assistant using FastAPI",
    version="1.0.0"
)

app.include_router(router)