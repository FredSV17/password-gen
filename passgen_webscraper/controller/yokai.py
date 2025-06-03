from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import status
from webscraper.webscraping_setup import start_webscraping


router = APIRouter()


@router.post("/webscraping",summary="Yokai name webscraping")
async def yokai_webscraping():
    await start_webscraping("YOKAI")
    return JSONResponse(status_code=status.HTTP_200_OK, content="")