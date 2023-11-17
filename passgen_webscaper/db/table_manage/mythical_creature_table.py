import json
from typing import List
from api.models.animal import AnimalModel
from api.models.mythical_creature import MythicalCreatureModel
from db.db_manager import db
from bson.json_util import loads,dumps
from fastapi.encoders import jsonable_encoder

async def insert_one_mythical_creature(mythical_creature: MythicalCreatureModel):
    mythical_creature_json_encoder = jsonable_encoder(mythical_creature)
    mythical_creature = db["mythical_creature"].insert_one(mythical_creature_json_encoder)
    return mythical_creature

#deprecated
def parse_json(data):
    return loads(dumps(data))


async def get_random_mythical_creature():
    cursor = db["mythical_creature"].aggregate([{ "$sample": { "size": 1 } }]).next()
    mythical_creature = cursor['name']
    return mythical_creature


def drop_collection_if_exists():
    if db["mythical_creature"] is not None:
        db["mythical_creature"].drop()