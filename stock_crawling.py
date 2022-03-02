import requests
from bs4 import BeautifulSoup

arr_Stock = [
    "005930",
    "000660",
    "035720",
    "054180",
    "099220"
]
# 삼성
# 에스케이하이닉스
# 카카오
for sotck in arr_Stock:
    url = f"https://finance.naver.com/item/main.nhn?code={sotck}"
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    sel = soup.find('p', "no_today").text
    # sel = sel.replace(',', '')
    selname = soup.find(
        'title').text
    sliceName = selname.split(':')[0]
    # relatedName = soup.find(
    #     'div', 'rate_info')
    # for i in relatedName:
    #     print(i.string)
    todayInfo = soup.find('div', {'class': 'today'}).text
    # find 찾기는 (태그값 , {속성값})
    print(sel, sliceName, todayInfo)


# res = requests.get("https://m.stock.naver.com/worldstock/stock/SDGR.O/total")
# html = res.text
# print(html)
