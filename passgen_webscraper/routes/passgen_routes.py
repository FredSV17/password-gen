from fastapi import APIRouter
from controller import animal
from controller import yokai
from controller import password_gen

api_router = APIRouter()

api_router.include_router(animal.router,prefix="/animal",tags=["animalWebscraping"])
api_router.include_router(yokai.router,prefix="/yokai",tags=["yokaiWebscraping"])
api_router.include_router(password_gen.router,prefix="/password",tags=["password"])