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

parser.add_argument('position', type=str, help='Prefered Job Position')
parser.add_argument('--location', type=str, default=None, help='Prefered Location')

args = parser.parse_args()

search_query = args.position
location = args.location

if location:
    search_query += f"&location={location}"


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

driver.get(f'https://www.linkedin.com/jobs/search/?keywords={search_query}')
time.sleep(5)

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# ul_element = soup.find('ul', class_='scaffold-layout__list-container')
job_listings = soup.find_all('div',{'class':'job-card-container'})
# print(job_listings)
job_data = []
for job in job_listings:
    try:
        job_position = job.find('strong').get_text().strip()
        job_id = job.get('data-job-id')
        img_url = job.find('img').get("src") if job.find("img") else None
        company = job.find('span', {'class': 'job-card-container__primary-description'}).get_text().strip()
        location = job.find('li', {'class': 'job-card-container__metadata-item'}).get_text().strip()
        job_data.append({
            "job_position": job_position,
            "job_id": job_id,
            "img_url": img_url,
            "company": company,
            "location": location,
        })
    except Exception as e:
        print(e)

time.sleep(10)
driver.quit()

with open('job_data.json', 'w') as json_file:
    json.dump(job_data, json_file, indent=2)

"https://www.linkedin.com/jobs/search/?currentJobId=3916958512"

"https://www.linkedin.com/search/results/people/?keywords=deepak harish"

"https://media.licdn.com/dms/image/C5603AQHNtCYOgnGQyA/profile-displayphoto-shrink_100_100/0/1632151149098?e=1721865600&v=beta&t=5E2pLOHu6gwSvkUKHRNs8hDwxtMnPwsYah4N8PiHq30"
"https://media.licdn.com/dms/image/C5603AQHNtCYOgnGQyA/profile-displayphoto-shrink_100_100/0/1632151149098?e=1721865600&amp;v=beta&amp;t=5E2pLOHu6gwSvkUKHRNs8hDwxtMnPwsYah4N8PiHq30"
"https://media.licdn.com/dms/image/C5603AQHNtCYOgnGQyA/profile-displayphoto-shrink_100_100/0/1632151149098?e=1721865600&v=beta&t=5E2pLOHu6gwSvkUKHRNs8hDwxtMnPwsYah4N8PiHq30"