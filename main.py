from time import sleep
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By


KEYWORDS = ['claude code', 'ux', 'devops', 'oracle', 'dart']

options = ChromeOptions()
options.add_argument('--headless')
driver = Chrome(options)
driver.get('https://habr.com/ru/all/')
sleep(5)

article_list = driver.find_element(By.CSS_SELECTOR, 'div.tm-articles-list')
articles = article_list.find_elements(By.CSS_SELECTOR,'div.article-snippet')

for article in articles:
    body = article.find_element(By.CSS_SELECTOR, 'div.article-formatted-body.article-formatted-body_version-2').text
    check = any(word in body.lower() for word in KEYWORDS)

    if check:
        header = article.find_element(By.CSS_SELECTOR, 'h2')
        a = header.find_element(By.CSS_SELECTOR, 'a')
        link = a.get_attribute('href')
        title = a.text.strip()

        article_date = article.find_element(By.CSS_SELECTOR, 'time').get_attribute('title').strip()

        print(f'{article_date} - {title} - {link}')
