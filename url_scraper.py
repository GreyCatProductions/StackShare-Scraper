from requests import get
from bs4 import BeautifulSoup

def get_all_urls(sitemap_urls: list[str]) -> list[str]:
    extracted_urls = []

    for url in sitemap_urls:
        response = get(url)

        if response.status_code == 200:
            text = response.text
            soup = BeautifulSoup(text, 'xml')
            links = [loc.text for loc in soup.find_all("loc")]
            extracted_urls.extend(links)
        else:
            print(f"Failed to get response from {url}")

    return extracted_urls