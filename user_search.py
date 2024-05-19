import argparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
import time
from bs4 import BeautifulSoup
import json
from config import *

parser = argparse.ArgumentParser()

parser.add_argument('username', type=str, help='Enter Username')
parser.add_argument('--pages', type=int, default=3, help='Total pages to search')
args = parser.parse_args()

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
time.sleep(2)

driver.find_element(By.NAME, "session_key")

username = driver.find_element(By.NAME, "session_key")
password = driver.find_element(By.NAME, "session_password")

username.send_keys(EMAIL)
password.send_keys(PASSWORD)

time.sleep(2)

submit = driver.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(5)

user_data = []
# user_count = 1
for page in range(1, args.pages+1):
    driver.get(f'https://www.linkedin.com/search/results/people/?keywords={args.username}&page={page}')
    time.sleep(5)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')

    users_list = soup.find_all('div',{'class':'ZrvZYtFWqnAXyAWKstvrcqbUDjCjkvndzDbLo'})
    if not users_list:
        break

    for user in users_list:
        try:
            img_url = user.find('img').get("src") if user.find("img") else None
            user_page_url = user.find("a", {'class': 'app-aware-link'}).get("href")
            name = user.find("span", {"dir": "ltr"}).find("span", {"aria-hidden": "true"}).get_text()
            _desc = user.find("div", {"class": "entity-result__primary-subtitle"})
            description = _desc.get_text().strip() if _desc else ""
            _loc = user.find("div", {"class": "entity-result__secondary-subtitle"})
            location = _loc.get_text().strip() if _loc else ""
            user_data.append({
                "name": name,
                "description": description,
                "location": location,
                "img_url": img_url,
                "user_page_url": user_page_url,
            })
            # user_count += 1
        except Exception as e:
            print(e)

with open('user_data.json', 'w') as json_file:
    json.dump(user_data, json_file, indent=2)

time.sleep(10)
driver.quit()
