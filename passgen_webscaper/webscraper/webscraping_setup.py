
from selenium import webdriver
from webscraper.get_data.webscraping_animal import get_animal_data
from webscraper.get_data.webscraping_mythical_creature import get_mythical_creature_data
from selenium.webdriver.chrome import options
from webdriver_manager.chrome import ChromeDriverManager

async def start_webscraping(type,url):
    #options.headless = True
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())#,options=options)

    driver.get(url)
    if type == "ANIMAL":
        await get_animal_data(driver)
    else:
        await get_mythical_creature_data(driver)
    driver.close()