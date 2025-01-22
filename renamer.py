import os
from bs4 import BeautifulSoup
import re
from time import sleep
from tqdm import tqdm

def extract_title(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as file:
        html_content = file.read()

    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.title.string.strip() if soup.title else "untitled"

def sanitize_filename(name: str):
    return re.sub(r'[\/:*?"<>|]', '_', name)

if __name__ == '__main__':
    folder_path = "data/19-01-2025"

    for child in tqdm(os.listdir(folder_path)):
        child_path = os.path.join(folder_path, child)

        if os.path.isfile(child_path):
            title = extract_title(child_path)
            sanitized_title = sanitize_filename(title)

            new_name = f"{sanitized_title}.html"
            new_path = os.path.join(folder_path, new_name)

            try:
                os.rename(child_path, new_path)
                # print(f"Renamed: {child} -> {new_name}")
            except Exception as e:
                print(f"Error renaming {child}: {e}")
