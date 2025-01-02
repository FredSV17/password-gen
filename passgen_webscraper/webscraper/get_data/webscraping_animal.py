from selenium.webdriver.common.by import By
import pandas
from logging_config import logger
from db.table_manage.animal_table import populate_animal_table_csv
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt) 
ANIMAL_WEBURL = 'https://en.wikipedia.org/wiki/List_of_animal_names'

# Needs work
async def get_animal_data(driver):
    driver.get(ANIMAL_WEBURL)
    # get the divs in selenium
    areas = driver.find_elements(By.XPATH,"//table")
    body = areas[2].find_element(By.TAG_NAME, 'tbody')
    rows = body.find_elements(By.TAG_NAME, 'tr')
    first_element_in_rows = [element.find_elements(By.TAG_NAME, 'td')[0].text
                            for element in rows if element.find_elements(By.TAG_NAME, 'td') != []]
    # Problem: Need to remove newline and any characters beyond
    new_list = list(map(lambda i: re.sub(r'([\n]|[^\w^ ]).*', '', i).strip(), first_element_in_rows))
    await populate_animal_table_csv(new_list)
    #name_list = navigate_through_areas(driver,areas,0)
    
    #populate_yokai_table_csv(name_list)
    return
    # div_results = driver.find_elements(By.XPATH,"//li")
    # animal_list = []
    # for div_result in div_results:
    #     animal_list = div_result.text.upper().split('\n')
    #     logger.debug(f'GOT(Sample): {animal_list[::5]}')
    #     df = pandas.DataFrame(data={"animal_names": animal_list})
    #     df.to_csv("./data/animal.csv",index=False)