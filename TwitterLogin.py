import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login(driver: webdriver, username, password):
    # Locate and interact with email/username field
    email_text = WebDriverWait(driver, 300).until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[text()='Telefonnummer, E-Mail-Adresse oder Nutzername']"))
    )
    email_field = email_text.find_element(By.XPATH, "ancestor::*[4]")
    time.sleep(1)
    email_field.click()
    driver.switch_to.active_element.send_keys(username)

    # Click "Weiter" to proceed
    next_button = WebDriverWait(driver, 300).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Weiter']/ancestor::*[2]"))
    )
    next_button.click()

    # Handle unusual activity prompt if it appears
    try:
        unusual_activity = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (By.XPATH, "//span[contains(text(), 'ungewöhnliche Anmeldeaktivität')]"))
        )
        driver.switch_to.active_element.send_keys(username)
        next_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//span[text()='Weiter']/ancestor::*[2]"))
        )
        next_button.click()
    except:
        pass

    time.sleep(1)

    driver.switch_to.active_element.send_keys(password)

    time.sleep(1)
    final_login_button = WebDriverWait(driver, 300).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[text()='Anmelden'])/ancestor::*[3]"))
    )
    final_login_button.click()
    time.sleep(3)

def scroll(driver, y_range):
    current_scroll = driver.execute_script("return window.scrollY;")
    time.sleep(0.1)

    max_scroll = driver.execute_script("return document.body.scrollHeight - window.innerHeight;")
    driver.execute_script(f"window.scrollBy(0, {y_range});")

    new_scroll = driver.execute_script("return window.scrollY;")

    return new_scroll != current_scroll and new_scroll < max_scroll