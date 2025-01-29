from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


def clickOkGotItButton(driver: WebDriver):
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Ok, got it']")))
    button.click()