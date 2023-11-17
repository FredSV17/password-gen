from api.models.mythical_creature import MythicalCreatureModel
from db.table_manage.mythical_creature_table import insert_one_mythical_creature
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

async def get_mythical_creature_data(driver):
    # BeautifulSoup(driver.find_elements(By.TAG_NAME,"li"))
    list_items_html = "\n".join([item.get_attribute("innerHTML") for item in driver.find_elements(By.TAG_NAME,"li")])

    list_items = BeautifulSoup(list_items_html,"html.parser").find_all("font")
    [await insert_one_mythical_creature(MythicalCreatureModel(name = mythical_creature.text.replace(" ","").upper())) for mythical_creature in list_items]