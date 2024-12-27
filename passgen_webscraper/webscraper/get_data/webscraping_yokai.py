from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas
from passgen_webscraper.db.table_manage.yokai_table import populate_yokai_table_csv
import re
from logging_config import logger

YOKAI = "https://yokai.com/finder/"

async def get_yokai_page(driver):
    driver.get(YOKAI)
    # get the divs in selenium
    areas = driver.find_elements(By.XPATH,"//div[@class='japanHtml5Map-areas-item']")
    name_list = navigate_through_areas(driver,areas,0)
    
    populate_yokai_table_csv(name_list)
    
    


def navigate_through_areas(driver, areas, curr_area=0):
    name_list = []
    if len(areas) == 0:
        return []
    area = areas[0].find_element(By.TAG_NAME,'a')
    # Scroll the element into view using JavaScript
    driver.execute_script("arguments[0].scrollIntoView(true);", area)
    logger.info(f'Visiting: {area.text}')
    WebDriverWait(driver, 10).until(
        # check if element is clickable
        EC.element_to_be_clickable(area)
    )
    area.click()
    name_list = get_yokai_data(driver)
    driver.get(YOKAI)
    
    next_area = curr_area+1
    areas = driver.find_elements(By.XPATH,"//div[@class='japanHtml5Map-areas-item']")[next_area:]
    name_list = name_list + navigate_through_areas(driver, areas, next_area)
    return name_list
    
# Get all the japanese prefectures
# For each japanese area (recursively)
#  - Click on the name
#  - Find all the yokai within that area
#  - Do any preprocessing that might be needed
#  - Save it on csv
def get_yokai_data(driver):
    # get the yokai names from the page
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    yokai_names = soup.find_all('article')
    yokai_list = [re.sub(r'^[\n ]+|[\n ]+$','',yokai_name.find('div').text) for yokai_name in yokai_names]
    logger.debug(f'GOT: {yokai_list}')
    # insert yokai names into the database
    return yokai_list