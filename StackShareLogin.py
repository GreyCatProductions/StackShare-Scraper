from selenium.webdriver.firefox.webdriver import WebDriver
from TwitterLogin import login as twitterLogin
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver: WebDriver):
    driver.get("https://stackshare.io")

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-testid="loginClick"]'))
    )
    button.click()

    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'seeMore'))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/users/auth/twitter"]'))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'submit'))
    )
    element.click()

    element = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'submit'))
    )
    element.click()

    twitterLogin(driver, "OlegShap05", "Twitter48311!")


