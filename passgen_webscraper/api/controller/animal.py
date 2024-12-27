from fastapi import APIRouter
from fastapi import Body
from fastapi.responses import JSONResponse
from fastapi import Body, status
from webscraper.webscraping_setup import start_webscraping

router = APIRouter()

@router.get("/hello",summary="Hello, start webscraping!")
def hello_from_animal():
    return "Hello from animal!"


#@router.post("/insert",summary="Animal name insert",response_model=AnimalModel)
#async def insert_animal(animal: AnimalModel = Body(...)):
#    new_animal = await insert_one(animal)
#    created_animal = await find_one(new_animal.inserted_id)
#    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_animal)


@router.post("/webscrape",summary="Animal name webscraping")
async def webscrape_animal():
    await start_webscraping("ANIMAL")
    return JSONResponse(status_code=status.HTTP_200_OK, content="")