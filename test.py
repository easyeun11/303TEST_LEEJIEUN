from bs4 import BeautifulSoup
from selenium import webdriver
import time
import csv

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%82%BC%EC%A9%9C%EC%82%BC&nso=so%3Add%2Cp%3Aall")

results = []
for page in range(1, 3):
    if page == 2:
        page_button = driver.find_element_by_link_text(str(2))
        page_button.click()
    articles = driver.find_elements_by_css_selector('.news_area > a')
    for article in articles:
        title = article.get_attribute('title')
        link = article.get_attribute('href')
        results.append([title, link])
        
with open('news.csv', mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['title', 'link'])
    writer.writerows(results)

driver.quit()