from bs4 import BeautifulSoup
from validator import valid_url
from requests import get

def load_sitemap_url_and_get_all_extracted_urls(sitemap_url: str) -> list[str]:
    if not valid_url(sitemap_url):
        print("Not a valid URL!")
        return []

    response = get(sitemap_url)

    if response.status_code == 200:
        text = response.text
        soup = BeautifulSoup(text, 'xml')
        links = [loc.text for loc in soup.find_all("loc")]
        return links
    else:
        print(f"Failed to get response from {sitemap_url}")
        return []
