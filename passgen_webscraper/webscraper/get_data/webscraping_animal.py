from selenium.webdriver.common.by import By
import pandas
from logging_config import logger

ANIMAL_WEBURL = 'https://en.wikipedia.org/wiki/List_of_animal_names'

# Needs work
async def get_animal_data(driver):
    driver.get(ANIMAL_WEBURL)
    # get the divs in selenium
    areas = driver.find_elements(By.XPATH,"//table")
    body = areas[2].find_element(By.TAG_NAME, 'tbody')
    rows = body.find_elements(By.TAG_NAME, 'tr')
    first_4_rows = [row.find_elements(By.TAG_NAME, 'td')[:3] for row in rows]
    
    #name_list = navigate_through_areas(driver,areas,0)
    
    #populate_yokai_table_csv(name_list)
    return 'Not implemented'
    # div_results = driver.find_elements(By.XPATH,"//li")
    # animal_list = []
    # for div_result in div_results:
    #     animal_list = div_result.text.upper().split('\n')
    #     logger.debug(f'GOT(Sample): {animal_list[::5]}')
    #     df = pandas.DataFrame(data={"animal_names": animal_list})
    #     df.to_csv("./data/animal.csv",index=False)