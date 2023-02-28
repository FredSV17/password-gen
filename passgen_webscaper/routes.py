from fastapi import APIRouter
from api.routes import animal
from api.routes import password_gen

api_router = APIRouter()

api_router.include_router(animal.router,prefix="/animal",tags=["animalScraper"])
api_router.include_router(password_gen.router,prefix="/password",tags=["password"])