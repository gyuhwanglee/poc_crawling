import requests
from bs4 import BeautifulSoup

url = "https://sports.news.naver.com/index"
res = requests.get(url)
html = res.text
soup = BeautifulSoup(html, 'html.parser')
news = soup.find('ul', 'today_list')
titleNewsName = news.find_all('strong', {'class': 'title'})
# 기사제목 가져오기
for i in titleNewsName:
    print(i.get_text())
# print(titleNewsName)
