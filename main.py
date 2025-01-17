import os
from datetime import datetime
import url_scraper
from website_downloader import download_page


def main():
    print("Starting to scrape all urls")
    scraped_urls = url_scraper.get_all_urls(site_map_urls)
    print(len(scraped_urls), "urls scraped")

    print("Starting to download all websites")
    failures = 0
    successes = 0
    for i, url in enumerate(scraped_urls):
        if i % 100 == 0:
            print(f"{i} / {len(scraped_urls)} websites downloaded")

        if download_page(url, save_location):
            successes += 1
        else:
            failures += 1

    print(f"successes: {successes}, failures: {failures}, total: {len(scraped_urls)}")

if __name__ == '__main__':
    save_location = os.path.join(os.getcwd(), 'data', datetime.today().strftime('%d-%m-%Y'))
    os.makedirs(save_location, exist_ok=True)
    site_map_urls = ["https://stackshare.io/sitemaps/stacks.xml", "https://stackshare.io/sitemaps/stacks2.xml", "https://stackshare.io/sitemaps/stacks3.xml"]
    main()