from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import status
from webscraper.webscraping_setup import start_webscraping


router = APIRouter()

@router.get("/hello",summary="Hello, start webscraping!")
def hello_from_yokai():
    return "Hello from yokai!"


#@router.post("/insert",summary="Mythical creature name insert",response_model=MythicalCreatureModel)
#async def insert_mythical_creature(mythical_creature: MythicalCreatureModel = Body(...)):
#    new_animal = await insert_one(mythical_creature)
#    created_animal = await find_one(new_animal.inserted_id)
#    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_animal)


@router.post("/webscraping",summary="Yokai name webscraping")
async def yokai_webscraping():
    await start_webscraping("YOKAI")
    return JSONResponse(status_code=status.HTTP_200_OK, content="")