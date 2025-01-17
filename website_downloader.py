import os.path
import requests

counter = 0

def download_page(url, save_location):
    global counter
    counter += 1
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join(save_location, f"site({counter}).html"), "w", encoding="utf-8") as file:
            file.write(response.text)
        return True
    else:
        print(f"Failed to retrieve the website. Status code: {response.status_code}")
        return False
