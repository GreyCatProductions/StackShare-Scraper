import os
import re
from time import sleep
import requests
from bs4 import BeautifulSoup


def download_page(url, save_location):
    response = get_response(url)

    if response and response.status_code == 200:
        try:
            os.makedirs(save_location, exist_ok=True)

            title = extract_title(response.text)
            safe_title = sanitize_filename(title)

            file_path = os.path.join(save_location, f"{safe_title}.html")

            with open(file_path, "w", encoding="utf-8") as file:
                file.write(response.text)
            print(f"Page saved: {file_path}")
            return True
        except Exception as e:
            print(f"Error saving page: {e}")
            return False
    else:
        print(f"Failed to retrieve the website after multiple attempts.")
        return False


def extract_title(file_text: str):
    soup = BeautifulSoup(file_text, 'html.parser')
    return soup.title.string.strip() if soup.title else "untitled"


def sanitize_filename(name: str):
    return re.sub(r'[\/:*?"<>|]', '_', name)


def get_response(url):
    retries = 5
    while retries > 0:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            # time sleep (3s? randfint 3-5) rand val * 6?
            # bs4 (BeautifulSoup4)
            # Check that there is a <script> that contains "StackProfile" in "id" attribute

            # Gleiches für:
            # https://stackshare.io/sitemaps/tools.xml
            # https://stackshare.io/sitemaps/tools2.xml
            # https://stackshare.io/sitemaps/tools3.xml
            # https://stackshare.io/sitemaps/tools4.xml
            # https://stackshare.io/sitemaps/companies.xml
            # https://stackshare.io/sitemaps/categories.xml
            # https://stackshare.io/sitemaps/functions.xml
            return response
        except requests.exceptions.Timeout:
            print(f"Request timed out for URL: {url}")
        except requests.exceptions.ConnectionError:
            print(f"Connection error for URL: {url}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download page {url}: {e}")
        retries -= 1
        if retries > 0:
            print(f"Retrying... ({retries} retries left)")
            sleep(10)
        else:
            print(f"Exhausted retries for URL: {url}")
    return None