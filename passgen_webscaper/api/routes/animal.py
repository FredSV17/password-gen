from fastapi import APIRouter
from api.api_models.animal import AnimalModel
from fastapi import Body
from fastapi.responses import JSONResponse
from fastapi import Body, status
from webscraper.animal.webscraping_animal import start_webscraping
from db.animal_table_manage.animal_table import insert_one, find_one, drop_collection


router = APIRouter()

@router.get("/hello",summary="Hello, start scraping!")
def hello_from_animal():
    return "Hello from animal!"


@router.post("/insert",summary="Animal name insert",response_model=AnimalModel)
async def insert_animal(animal: AnimalModel = Body(...)):
    new_animal = await insert_one(animal)
    created_animal = await find_one(new_animal.inserted_id)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_animal)


@router.post("/webscrape",summary="Animal name webscraping")
async def webscrape_animal():
    # drop_collection()
    await start_webscraping()
    return JSONResponse(status_code=status.HTTP_200_OK, content="")