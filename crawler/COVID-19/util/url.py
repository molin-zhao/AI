import requests
import time
from selenium import webdriver
from bs4 import BeautifulSoup

requests.adapters.DEFAULT_RETRIES = 5

# get html from url
def get_url(url, headers):
    session = requests.session()
    session.keep_alive = False
    html = session.get(url, headers=headers)
    print(html)
    html.encoding = "UTF-8"
    soup = BeautifulSoup(html.text, "html.parser")
    return soup

# gen cookie
def get_cookie(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    cookies = driver.get_cookies()
    driver.quit()
    items = []
    for i in range(len(cookies)):
        cookie_value = cookies[i]
        item = cookie_value['name'] + '=' + cookie_value['value']
        items.append(item)
    cookie_str = '; '.join(i for i in items)
    return cookie_str    

