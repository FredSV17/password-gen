from fastapi import APIRouter
from fastapi import Body
from fastapi.responses import JSONResponse
from fastapi import Body, status
from webscraper.webscraping_setup import start_webscraping

router = APIRouter()

@router.post("/webscrape",summary="Animal name webscraping")
async def webscrape_animal():
    await start_webscraping("ANIMAL")
    return JSONResponse(status_code=status.HTTP_200_OK, content="")