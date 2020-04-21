from bs4 import BeautifulSoup
import requests

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://series.naver.com/novel/detail.nhn?productNo=1200383',headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')
soup.find(' ul.comment_focus > li')

for review in reviews:
    content = review.select_one('p')
    print(review)
#1. nick name 가져오기
#2. 내용 가져오기(cbox)
#3. 가져온 자료 보이게 하기 







