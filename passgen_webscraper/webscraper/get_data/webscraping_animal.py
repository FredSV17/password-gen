from api.api_models.animal import AnimalModel
from db.table_manage.animal_table import insert_one
from selenium.webdriver.common.by import By
import pandas
from logging_config import logger

ANIMAL_WEBURL = "https://a-z-animals.com/animals/"

async def get_animal_data(driver):
    driver.get(ANIMAL_WEBURL)
    div_results = driver.find_elements(By.XPATH,"//li")
    animal_list = []
    for div_result in div_results:
        animal_list = div_result.text.upper().split('\n')
        logger.debug(f'GOT(Sample): {animal_list[::5]}')
        df = pandas.DataFrame(data={"animal_names": animal_list})
        df.to_csv("./data/animal.csv",index=False)