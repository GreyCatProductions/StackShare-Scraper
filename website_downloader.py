import os
from time import sleep
import requests


def download_page(url, save_location):
    response = get_response(url)

    if response and response.status_code == 200:
        try:
            os.makedirs(save_location, exist_ok=True)

            counter = len(os.listdir(save_location)) + 1
            file_path = os.path.join(save_location, f"site({counter}).html")

            with open(file_path, "w", encoding="utf-8") as file:
                file.write(response.text)
            return True
        except Exception as e:
            return False
    else:
        print(f"Failed to retrieve the website after multiple attempts.")
        return False

def get_response(url):
    retries = 5

    while retries > 0:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            print(f"Request timed out or connection error for URL: {url}")
            sleep(300)
        except Exception as e:
            print(f"Failed to download page {url}: {e}")
        retries -= 1
        if retries > 0:
            print(f"Retrying... ({retries} retries left)")
            sleep(10)
    return None