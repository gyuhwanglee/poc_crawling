import requests
from bs4 import BeautifulSoup
import json


url = 'https://restful-booker.herokuapp.com/auth'  # post token 생성
url2 = 'https://restful-booker.herokuapp.com/booking'  # get booking
url3 = 'https://restful-booker.herokuapp.com/ping'  # Ping - HealthCheck

url5 = 'https://restful-booker.herokuapp.com/booking'  # CreateBooking

# booking = requests.get(url2)
# html2 = booking.text
# print(html2)

header = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    "User-Agent": "{'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ''(KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'}",
}
data = {
    "username": "admin",
    "password": "password123"
}

createToken = requests.post(url, json=header, data=data)  # login
createRes = createToken.status_code  # status_code 값 얻어오기
createRes = createToken.content  # contents속성을 이용해 값 얻어오기
print('createToken', createRes)
createHeader = createToken.headers  # header의 담기는 값을 확인
# print(createHeader)
createTokenHtml = createToken.text
print('token값 확인', createTokenHtml)  # token 값 확인
html = createToken.text
soup = BeautifulSoup(html, 'html.parser')
print(html)

# booking 확인
url4 = f'https://restful-booker.herokuapp.com/booking/20'


create_data = {
    "firstname": "el",
    "lastname": "hwang",
    "totalprice": 123456,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"
}

headers1 = {
    "Content-Type": "application/json"
}
# 예약하기 - 왜 두번째 인자를 json 이라는 변수명으로 보내야 하는가?
createBooking = requests.post(url5, json=create_data)
createBookingRes = createBooking.content
bookingId = createBooking.text
print('???what??', bookingId)
# createBookingHtml = createBooking.text
print('CreateBooking확인', createBookingRes)

checkBooking = requests.get('https://restful-booker.herokuapp.com/booking/124')
checkBookingHtml = checkBooking.text
checkHeader = checkBooking.headers
checkContent = checkBooking.content
print('booking체크체크', checkContent)
print(checkHeader)
# print(checkBookingHtml)


header = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Cookie': 'token=546b325b4fc00ad',
}
patch_data = {
    "firstname": "Jimeeee",
    "lastname": "Brown",
    "totalprice": 11111,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2018-01-01",
        "checkout": "2019-01-01"
    },
    "additionalneeds": "Breakfast"

}
putBooking = requests.put(
    'https://restful-booker.herokuapp.com/booking/124', headers=header, data=json.dumps(patch_data))
# putHtml = putBooking.text
putRes = putBooking.status_code
putHeader = putBooking.headers
putData = putBooking.content.decode('utf-8')
# print('content', putData)
# print('header', putHeader)
# print(putData)
print(putRes)


# deleteBooking = requests.delete(url4, headers=header)
# deleteRes = deleteBooking.status_code
# print(deleteRes)


# pingHealthCheck = requests.get(url3)
# pingHealthCheckRes = pingHealthCheck.content
# # html3 = pingHealthCheck.text
# print('PIngHealthCheck', pingHealthCheckRes)
