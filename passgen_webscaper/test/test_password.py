import re
from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest
from api.api_models.animal import AnimalModel

from db.db_manager import drop_database
from db.animal_table_manage.animal_table import insert_one

from main import app
import pytest

client = TestClient(app)


sample_animals = ['PYTHON','EAGLE','BEAR']


@pytest.fixture
async def setup_database():
    [await insert_one(AnimalModel(name = animal)) for animal in sample_animals]

@pytest.mark.asyncio
async def test_generate_password(setup_database):
    await setup_database
    response = client.get("/password/generate")
    assert response.status_code == 200
    assert any(word.lower() in response.content.decode() for word in sample_animals)

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
async def test_generate_password_check_camelcase(setup_database):
    await setup_database
    response = client.get("/password/generate?parts_of_speech=A")
    assert response.status_code == 400

@pytest.mark.asyncio
async def test_generate_password(setup_database):
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