import requests
from bs4 import BeautifulSoup

def get_exchange_rate(target1, target2): #헤더는 내가 어느방법으로 접속하는지 알려주는 정보임. 아무정보 없이 접속하면 차단시킴.
    headers = {
        'User-Agent': 'Mozilla/5.9',
        'Content-Type': 'text/html; charset=utf-8'
    }
#크롤링
    response = requests.get("http://kr.investing.com/currencies/{}-{}".format(target1, target2), headers=headers)
    content = BeautifulSoup(response.content, 'html.parser')
    containers = content.find('span', {'data-test': 'instrument-price-last'})
#크롬 인베스팅 닷컴 들어가서 F12누르고 찾을 수 있다. #크롤링 막을려고 맨날 바꾼다. 그래서 API사용해야함.
    print(containers.text) #나중에 크롤링에서 배우자.


get_exchange_rate('usd', 'krw')
