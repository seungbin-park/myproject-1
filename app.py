
from bs4 import BeautifulSoup
import requests

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

 

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://series.naver.com/novel/top100List.nhn',headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')
novels = soup.select('ul.comic_top_lst > li')
for novel in novels:
    image = novel.select_one('a > img')
    print(image['src'])


