from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium import webdriver

def createDriver():
    service = Service()
    options = Options()
    driver = webdriver.Firefox(service=service, options=options)
    driver.set_page_load_timeout(10)
    driver.maximize_window()
    return driver