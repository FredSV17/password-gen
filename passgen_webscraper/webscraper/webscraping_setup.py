
from selenium import webdriver
from webscraper.get_data.webscraping_animal import get_animal_data
from webscraper.get_data.webscraping_yokai import get_yokai_page
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

async def start_webscraping(type):
    #options.headless = True
    

    # Optional: Configure Chrome options (e.g., headless mode)
    # Set up Chrome options for headless mode
    chrome_options = Options()
    #chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (optional but recommended)
    chrome_options.add_argument("--window-size=1920x1080")  # Set window size (helps with rendering issues)


    # Initialize the Chrome WebDriver with the Service object and options
    driver = webdriver.Chrome(options=chrome_options)
    
    if type == "ANIMAL":
        await get_animal_data(driver)
    if type == "YOKAI":
        await get_yokai_page(driver)
    driver.close()