from fastapi import APIRouter
from api.models.mythical_creature import MythicalCreatureModel
from fastapi import Body
from fastapi.responses import JSONResponse
from fastapi import Body, status
from webscraper.webscraping_setup import start_webscraping
from db.table_manage.mythical_creature_table import drop_collection_if_exists


router = APIRouter()
MYTHICAL_CREATURE = "https://www.mythicalcreaturesguide.com/list-of-mythical-creatures/"
@router.get("/hello",summary="Hello, start webscraping!")
def hello_from_mythical_creature():
    return "Hello from mythical creature!"


#@router.post("/insert",summary="Mythical creature name insert",response_model=MythicalCreatureModel)
#async def insert_mythical_creature(mythical_creature: MythicalCreatureModel = Body(...)):
#    new_animal = await insert_one(mythical_creature)
#    created_animal = await find_one(new_animal.inserted_id)
#    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_animal)


@router.post("/webscraping",summary="Mythical creature name webscraping")
async def mythical_creature_webscraping():
    drop_collection_if_exists()
    await start_webscraping("MYTHICAL_CREATURE",MYTHICAL_CREATURE)
    return JSONResponse(status_code=status.HTTP_200_OK, content="")