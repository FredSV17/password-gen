from re import sub
from typing import List, Optional
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi import status
from db.animal_table_manage.animal_table import get_random_one
from wonderwords import RandomWord
from random import randint
import names

router = APIRouter()

@router.get("/hello",summary="Hello, start scraping!")
def hello_from_animal():
    return "Hello from animal!"


@router.get("/generate",summary="Password gen")
async def password_gen(substantive_type: Optional[str] = "ANIMAL",parts_of_speech: Optional[str] = "verb;adjective", separator: Optional[str] = "_",special_character: Optional[str] = "@",min_num_rand: Optional[int] = 1,max_num_rand: Optional[int] = 100):
    r = RandomWord()

    parts_of_speech_list = parts_of_speech.split(';')

    try:
        substantive = await handle_substantive_type(substantive_type)
    except:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="INVALID SUBSTANTIVE")


    try:
        word = r.word(include_parts_of_speech=parts_of_speech_list)
    except:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="ERROR INVALID PART OF SPEECH")
    
    sentence = handle_separators(f'{word} {substantive}', separator)
    if min_num_rand > max_num_rand:
            return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content="MIN GREATER THAN MAX")
    password = f'{sentence}{special_character}{str(randint(min_num_rand,max_num_rand))}'
    return JSONResponse(status_code=status.HTTP_200_OK, content=password)

def handle_separators(sentence, separator):
    if separator == "CAMELCASE":
        return sub(r"(_|-)+", " ", sentence).title().replace(" ", "")
    else:
        return sentence.replace(" ",separator).lower()

async def handle_substantive_type(substantive_type: str):
    if substantive_type == "ANIMAL":
        return await get_random_one()
    elif substantive_type == "PERSON":
        return names.get_full_name()
    elif substantive_type == "NOUN":
        r = RandomWord()
        return r.word(include_parts_of_speech=['noun'])
    elif substantive_type == "RANDOM":
        rand = randint(1,3)
        if rand == 2:
            return names.get_full_name()
        elif rand == 3:
            r = RandomWord()
            return r.word(include_parts_of_speech=['noun'])
        else:
            return await get_random_one()
    else:
        raise Exception