from db.db_manager import db
from bson.json_util import loads,dumps
import csv
import random
from pandas import DataFrame
import pandas


ANIMAL_TABLE = 'passgen_webscraper/data/animal.csv'

async def get_random_animal():
    with open(ANIMAL_TABLE) as f:
        reader = csv.reader(f)
        return random.choice(list(reader))
    
async def populate_animal_table_csv(name_list: list):
    df = pandas.DataFrame(data={"animal": name_list})
    df.to_csv("./data/animal.csv",index=False)