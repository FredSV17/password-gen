from fastapi.testclient import TestClient
import os
import pytest
from api.api_models.animal import AnimalModel

os.environ["API_TEST"] = "1"
from db.db_manager import drop_database
from db.animal_table_manage.animal_table import insert_one,find_one

from main import app

client = TestClient(app)
sample_animals = ['python','eagle','bear']

@pytest.fixture
async def setup_database():
    [await insert_one(AnimalModel(name = animal)) for animal in sample_animals]

# @pytest.fixture(scope="session", autouse=True)
# def cleanup():
#     drop_database()
# Arrange
# @pytest.fixture
# def order(first_entry):
#     return [first_entry]