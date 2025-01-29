import os
import re
import bs4
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.webdriver import WebDriver
from saver import save_to_csv

def extract_title(soup: BeautifulSoup):
    return soup.title.string.strip() if soup.title else "untitled"

def sanitize_filename(name: str):
    return re.sub(r'[/:*?"<>|]', '_', name)

def process_website(driver: WebDriver, dir_path: os.path):
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    try:
        data = {
            "Name": sanitize_filename(extract_title(soup)),
            "Application and Data": get_frameworks(soup, "Application and Data"),
            "Utilities": get_frameworks(soup, "Utilities"),
            "DevOps": get_frameworks(soup, "DevOps"),
            "Business Tools": get_frameworks(soup, "Business Tools"),
        }
    except Exception as e:
        print(f"failed to get frameworks: {e}")
        return False

    try:
        save_to_csv(data, dir_path)
    except Exception as e:
        print(f"failed to save data: {e}")
        return False
    return True

def get_frameworks(soup: BeautifulSoup, name: str):
    try:
        application_and_data_text = soup.find(string=name)
        application_and_data_parent = application_and_data_text.parent.parent.parent
        application_and_data_framework_container = application_and_data_parent.contents[1]
        names = []

        if not isinstance(application_and_data_framework_container, bs4.Tag):
            raise TypeError("Expected a Tag but found a different type.")

        for child in application_and_data_framework_container.contents:
            if not isinstance(child, bs4.Tag):
                raise TypeError("Expected a Tag but found a different type.")
            name = child.contents[1].text
            names.append(name)
        return names
    except:
        return []
