from bs4 import BeautifulSoup
import requests
from selenium import webdriver

import os
import time

options = webdriver.ChromeOptions() 
options.add_argument('headless') 
options.add_argument('window-size=1920x1080') 
options.add_argument("disable-gpu") 

path = os.path.dirname(__file__)
driver = webdriver.Chrome(path + '/chromedriver', options=options)

# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://series.naver.com/novel/detail.nhn?productNo=1200383',headers=headers)

driver.get('https://series.naver.com/novel/detail.nhn?productNo=1200383')
time.sleep(2)

# 해당 페이지의 html 소스 선택
html = driver.page_source
# html 파싱하기
soup = BeautifulSoup(html, 'html.parser')
comments = soup.select_one('#comment_focus')

for review in comments.select('div.cbox_comment_area'):
    #1. nick name 가져오기
    nick_name = review.select_one("span.cbox_nick_name").text

    #2. 내용 가져오기(cbox)
    content = review.select_one("div.cbox_desc_comment>p").text

    #3. 가져온 자료 보이게 하기(??)
    print(nick_name, content)

driver.quit()
