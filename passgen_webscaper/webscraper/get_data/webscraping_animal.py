from api.models.animal import AnimalModel
from db.table_manage.animal_table import insert_one_animal
from selenium.webdriver.common.by import By


async def get_animal_data(driver):
        div_results = driver.find_elements(By.XPATH,"//div[@class='container']")
        for div_result in div_results:
            animal_list = div_result.text.upper().split('\n')
            [await insert_one_animal(AnimalModel(name = animal)) for animal in animal_list]