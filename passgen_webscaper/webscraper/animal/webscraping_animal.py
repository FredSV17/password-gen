from api.api_models.animal import AnimalModel
from db.animal_table_manage.animal_table import insert_one
from webscraper.webscraping_URLS import ANIMAL_WEBURL
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.options import Options

async def start_webscraping():
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options)

    driver.get(ANIMAL_WEBURL)
    await _get_data(driver)
    driver.close()

async def _get_data(driver):
        div_results = driver.find_elements(By.XPATH,"//div[@class='container']")
        for div_result in div_results:
            animal_list = div_result.text.upper().split('\n')
            [await insert_one(AnimalModel(name = animal)) for animal in animal_list]