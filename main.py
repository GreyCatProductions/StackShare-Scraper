import os
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

import StackShareLogin
from driverFactory import createDriver

def main():
    print("Trying to create driver")
    driver = None
    try:
        driver = createDriver()
        print("Driver created")
    except Exception as e:
        print("Failed to create driver " + str(e))

    print("Trying to login")
    try:
        StackShareLogin.login(driver)
        print("Login successful")
    except Exception as e:
        print("Login failed " + str(e))

    try:
        button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[text()='Ok, got it']")))
        button.click()
    except:
        pass



if __name__ == '__main__':
    save_location = os.path.join(os.getcwd(), 'data', datetime.today().strftime('%d-%m-%Y'))
    os.makedirs(save_location, exist_ok=True)
    site_map_urls = ["https://stackshare.io/sitemaps/stacks.xml", "https://stackshare.io/sitemaps/stacks2.xml", "https://stackshare.io/sitemaps/stacks3.xml"]
    main()