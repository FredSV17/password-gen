from fastapi import APIRouter
from api.models.animal import AnimalModel
from fastapi import Body
from fastapi.responses import JSONResponse
from fastapi import Body, status
from webscraper.webscraping_setup import start_webscraping
from db.table_manage.animal_table import drop_collection_if_exists


router = APIRouter()
ANIMAL_WEBURL = "https://a-z-animals.com/animals/"

@router.get("/hello",summary="Hello, start webscraping!")
def hello_from_animal():
    return "Hello from animal!"


#@router.post("/insert",summary="Animal name insert",response_model=AnimalModel)
#async def insert_animal(animal: AnimalModel = Body(...)):
#    new_animal = await insert_one(animal)
#    created_animal = await find_one(new_animal.inserted_id)
#    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_animal)


@router.post("/webscraping",summary="Animal name webscraping")
async def animal_webscraping():
    drop_collection_if_exists()
    await start_webscraping("ANIMAL",ANIMAL_WEBURL)
    return JSONResponse(status_code=status.HTTP_200_OK, content="")