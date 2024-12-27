import motor.motor_asyncio
import os
import pymongo

MONGODB_URL_HC = 'mongodb://root:example@localhost/local?retryWrites=true&w=majority&authSource=admin'
os.environ["API_TEST"] = "0"
# client = pymongo.MongoClient(os.environ["MONGODB_URL"])
client = pymongo.MongoClient(MONGODB_URL_HC)
if os.environ["API_TEST"] == True:
    db = client["testpasswordgen"]
else:    
    db = client["passwordgen"]

def drop_database():
    client.drop_database("testpasswordgen")