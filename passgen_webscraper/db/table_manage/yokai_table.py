from db.db_manager import db
from bson.json_util import loads,dumps
from fastapi.encoders import jsonable_encoder
import csv
import random
import pandas

YOKAI_TABLE = 'passgen_webscraper/data/yokai.csv'

async def get_random_yokai():
    with open(YOKAI_TABLE) as f:
        reader = csv.reader(f)
        return random.choice(list(reader))
    
async def populate_yokai_table_csv(name_list: list):
    df = pandas.DataFrame(data={"yokai_names": name_list})
    df.to_csv("./data/animal.csv",index=False)