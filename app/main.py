from fastapi import FastAPI
from app.api.endpoints import router as translation_router

app = FastAPI()

# Include the translation routes
app.include_router(translation_router, prefix="/translation", tags=["translation"])
