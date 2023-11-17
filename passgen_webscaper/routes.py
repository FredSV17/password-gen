from fastapi import APIRouter
from api.controller import animal
from api.controller import mythical_creature
from api.controller import password_gen

api_router = APIRouter()

api_router.include_router(animal.router,prefix="/animal",tags=["animalWebscraping"])
api_router.include_router(mythical_creature.router,prefix="/mythical_creature",tags=["mythicalCreatureWebscraping"])
api_router.include_router(password_gen.router,prefix="/password",tags=["password"])