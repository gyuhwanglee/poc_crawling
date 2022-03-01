import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/main.nhn?code=005930"
res = requests.get(url)
html = res.text
soup = BeautifulSoup(html, 'html.parser')
sel = soup.find('div', "today").text
sel = sel.replace(',', '')
print(sel)


# res = requests.get("https://m.stock.naver.com/worldstock/stock/SDGR.O/total")
# html = res.text
# print(html)
