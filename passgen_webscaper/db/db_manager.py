import motor.motor_asyncio
import os
import pymongo

client = pymongo.MongoClient(os.environ["MONGODB_URL"])

if os.environ["API_TEST"] == "1":
    db = client["testpasswordgen"]
else:    
    db = client["passwordgen"]

def drop_database():
    client.drop_database("testpasswordgen")