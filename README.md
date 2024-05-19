# LinkedIn Scrapper

## Requirements
1. Latest Updated version of Google Chrome Browser
2. Python 3.10+

## Folder Structure
```
linkedin_scripts/
├── chromedriver.exe
├── config.py
├── job_search.py
├── requirements.txt
└── user_search.py
```

## Project setup
### 1. Create virtual environment
```
cd linkedin_scripts/
```
```
python -m venv venv
```
or
```
python3 -m venv venv
```

### 2. Activate virtual environment

For Windows
```
 .\venv\Scripts\activate
```
For Mac and Linux
```
source venv/bin/activate
```

### 3. Install Required Packages
All the packages are mentioned in `requirements.txt` file. To install:
```
pip install -r requirements.txt
```

### 4. Config
Enter your email and password in the `config.py` file.
```python
EMAIL = "<your email>"
PASSWORD = "<your password>"
```

## User Search
For searching users run `user_search.py` file with following command.
```
python user_search.py "John Doe"
```
If you want to search upto nth page you can run this command.
```
python user_search.py "John Doe" --pages 10
```
by default `--pages` is set to 3

The above command will run and give you the users list in a json file named `user_data.json`
```json
[
...
  {
    "name": "John Doe",
    "description": "Business Analyst at L&T IDPL",
    "location": "Tamil Nadu, India",
    "img_url": "<image url>",
    "user_page_url": "<user profile url>"
  }
...
]
```

## Jobs Search
For searching jobs run `job_search.py` file with following command.
```
python job_search.py "python developer"
```
If you want to mention location you can use 
```
python job_search.py "react developer" --location "Chennai"
```
The above command will give you the jobs list in a json file named `job_data.json`
```json
[
...
  {
    "job_position": "React Js Developer",
    "job_id": "3911012080",
    "img_url": "https://media.licdn.com/dms/image/D4D0BAQGsGR9p4ikS5w/company-logo_100_100/0/1708946550425/tata_consultancy_services_logo?e=1724284800&v=beta&t=m2mm3IRj2sQcWt5O9mo0peq04RZT1CKkZexDzUPqiHg",
    "company": "Tata Consultancy Services",
    "location": "Chennai, Tamil Nadu, India (On-site)"
  }
...
]
```