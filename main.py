import os
import random
import time
from datetime import datetime
from selenium.common import TimeoutException
from driver_factory import createDriver
from sitemap_extractor import load_sitemap_url_and_get_all_extracted_urls
from site_data_extractor import process_website
from tqdm import tqdm

def main():
    print("Trying to create driver")
    driver = createDriver()
    print("Driver created")

    total_successes = 0
    total_failures = 0
    for site_map_url in site_map_urls[:]:
        successes = 0
        failures = 0
        urls = get_urls_safely(site_map_url)
        dir_path = os.path.join(save_location, get_last_part_of_url(site_map_url))

        for url in tqdm(urls):
            retries = 5
            while retries > 0:
                try:
                    driver.get(url)
                    time.sleep(random.uniform(0.75, 2))
                    success = process_website(driver, dir_path)
                    if success:
                        break
                    else:
                        print(f"Failed to extract data from {url}")
                        retries -= 1
                except TimeoutException:
                    print("timed out!")
                    time.sleep(300)

            if retries > 0:
                successes += 1
            else:
                failures += 1
            time.sleep(random.uniform(0.5, 3))

        total_successes += successes
        total_failures += failures
        print(f"Finished scraping {site_map_url}. Successes: {successes}, Failures: {failures} ({round(successes / (successes + failures) * 100), 2}%)")
    print(f"Scrape finished. Successes: {total_successes}, Failures: {total_failures} ({round(total_successes / (total_successes + total_failures) * 100), 2}%)")

def get_urls_safely(url: str):
    retries = 3
    while retries > 0:
        urls = load_sitemap_url_and_get_all_extracted_urls(url)
        if len(urls) > 0:
            return urls
        retries -= 1

def get_last_part_of_url(url:str) -> str:
    return (url.split('/')[-1]).split('.')[0]

if __name__ == '__main__':
    save_location = os.path.join(os.getcwd(), 'data', datetime.today().strftime('%d-%m-%Y'))
    os.makedirs(save_location, exist_ok=True)
    site_map_urls = ["https://stackshare.io/sitemaps/stacks.xml",
                     "https://stackshare.io/sitemaps/stacks2.xml",
                     "https://stackshare.io/sitemaps/stacks3.xml",
                     #"https://stackshare.io/sitemaps/tools.xml",
                     #"https://stackshare.io/sitemaps/tools2.xml",
                     #"https://stackshare.io/sitemaps/tools3.xml",
                     #"https://stackshare.io/sitemaps/tools4.xml",
                     #"https://stackshare.io/sitemaps/companies.xml",
                     #"https://stackshare.io/sitemaps/categories.xml",
                     #"https://stackshare.io/sitemaps/functions.xml"
                     ]
    main()