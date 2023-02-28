import json
from typing import List
from api.api_models.animal import AnimalModel
from db.db_manager import db
from bson.json_util import loads,dumps
from fastapi.encoders import jsonable_encoder

async def insert_one(animal: AnimalModel):
    animal_json_encoder = jsonable_encoder(animal)
    new_animal = db["animal"].insert_one(animal_json_encoder)
    return new_animal

def parse_json(data):
    return loads(dumps(data))

async def find_one(id: str):    
    found_animal = db["animal"].find_one({"_id": id})
    return found_animal

async def get_random_one():    
    cursor = db["animal"].aggregate([{ "$sample": { "size": 1 } }]).next()
    animal = cursor['name']
    return animal


def drop_collection():
    db["animal"].drop()