import re
from fastapi import FastAPI
from fastapi.testclient import TestClient

from api.models.animal import AnimalModel
from api.models.mythical_creature import MythicalCreatureModel

from db.db_manager import drop_database
from db.table_manage.animal_table import insert_one_animal
from db.table_manage.mythical_creature_table import insert_one_mythical_creature
import os
os.environ["API_TEST"]="1"
from main import app
import pytest

client = TestClient(app)


sample_animals = ['PYTHON','EAGLE','BEAR']
sample_mythical_creatures = ['DRAGON','CENTAUR','MEDUSA']



@pytest.fixture
async def setup_database():
    [await insert_one_animal(AnimalModel(name = animal)) for animal in sample_animals]
    [await insert_one_mythical_creature(MythicalCreatureModel(name = mythical_creature)) for mythical_creature in sample_mythical_creatures]

@pytest.mark.asyncio
async def test_generate_password_animal(setup_database):
    await setup_database
    response = client.get("/password/generate?substantive_type=ANIMAL")
    assert response.status_code == 200
    assert any(word.lower() in response.content.decode() for word in sample_animals)

@pytest.mark.asyncio
async def test_generate_password_mythical_creature(setup_database):
    await setup_database
    response = client.get("/password/generate?substantive_type=MYTHICAL_CREATURE")
    assert response.status_code == 200
    assert any(word.lower() in response.content.decode() for word in sample_mythical_creatures)

@pytest.mark.asyncio
async def test_generate_password_with_min_greater_than_max(setup_database):
    await setup_database
    response = client.get("/password/generate?min_num_rand=1000&max_num_rand=1")
    assert response.status_code == 400

@pytest.mark.asyncio
async def test_generate_password_check_separator(setup_database):
    await setup_database
    separator = ()
    response = client.get(f"/password/generate?separator={separator}")
    assert response.status_code == 200
    text = response.content.decode().replace("\"","")
    assert re.match(r"([a-z]{2,}\(\)){1,}(.*)", text)

@pytest.mark.asyncio
async def test_generate_password_check_invalid_substantive_type(setup_database):
    await setup_database
    response = client.get("/password/generate?substantive_type=A")
    assert response.status_code == 400

@pytest.mark.asyncio
async def test_generate_password_check_invalid_parts_of_speech(setup_database):
    await setup_database
    response = client.get("/password/generate?parts_of_speech=A")
    assert response.status_code == 400


@pytest.mark.asyncio
async def test_generate_password_check_camelcase(setup_database):
    await setup_database
    response = client.get("/password/generate?parts_of_speech=A")
    assert response.status_code == 400

@pytest.mark.asyncio
async def test_generate_password_camelcase(setup_database):
    await setup_database
    response = client.get("/password/generate?separator=CAMELCASE")
    assert response.status_code == 200
    text = response.content.decode().replace("\"","")
    assert re.match(r"([A-Z][a-z]{2,}){1,}(.*)", text)



@pytest.fixture(scope="session", autouse=True)
def cleanup(request):
    """Cleanup a testing directory once we are finished."""
    def remove_test_dir():
        drop_database()
    request.addfinalizer(remove_test_dir)