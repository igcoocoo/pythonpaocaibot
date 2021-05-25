import urllib.request
from bs4 import BeautifulSoup

#url 앰종고에 있는 html을 긁어온다.
url = 'http://yeongjong.icehs.kr/foodlist.do?m=020701&s=yeongjong'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find(class_='today')

print(title.text)


#토큰값 mgqwn283rRwlkVqTggJJNUwV7OFRPQAE850cFsCZrnF


# 라인으로 메세지를 보낸다
import requests
try:

    TARGET_URL = 'https://notify-api.line.me/api/notify'
    TOKEN = 'mgqwn283rRwlkVqTggJJNUwV7OFRPQAE850cFsCZrnF'

    response = requests.post(
        TARGET_URL,
        headers={
            'Authorization': 'Bearer ' + TOKEN
        },
        data={
            'message': title.text
        }
    )

except Exception as ex:
    print(ex)
