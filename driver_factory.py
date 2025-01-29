from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium import webdriver

def createDriver():
    service = Service()
    options = Options()
    driver = webdriver.Firefox(service=service, options=options)
    driver.maximize_window()
    driver.set_page_load_timeout(60)
    return driver