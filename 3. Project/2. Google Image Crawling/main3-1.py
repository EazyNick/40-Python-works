#!/usr/bin/env python
# coding: utf-8

# In[39]:


#selenium 웹을 제어하는 유명한 라이브러리
#webdriver-manager 웹드라이버에 사용하는 크롬드라이브 파일을 손쉽게 다운로드 할 수 있는 라이브러리
#nbconvert 주피터 -> .py로 변환 
#이 3가지 라이브러리 pip insatall 하고 시작합니다.
#주피터를 쓰는 이유? - 

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
driver = webdriver.Chrome(ChromeDriverManager().install())
#이러면 크롬 다운로드 되고 창을 하나 띄움. 경로 지정을 하기위해 이걸로 깔아준 것.

URL = "https://www.google.co.kr/imghp?hl=ko" #구글 이미지 검색하는 URL
driver.get(url=URL)

driver.implicitly_wait(time_to_wait=10) #열릴때까지 최대 10초 기다려라. 그전에 열리면 빠져나옴.


# In[40]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#크롬(이미지 검색창)에서 F12를 눌러보자
#누르고 검색창 부분의 코드를 찾고 Copy select

elem = driver.find_element(By.CSS_SELECTOR,"body > div.L3eUgb > div.o3j99.ikrT4e.om7nvf > form > div:nth-child(1) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input")
elem.send_keys('바다') #검색
elem.send_keys(Keys.RETURN) #엔터


# In[41]:


import time
elem = driver.find_element(By.TAG_NAME, "body") #창 안에 있는걸 body라함
for i in range(60):
    elem.send_keys(Keys.PAGE_DOWN) #페이지 다운키를 계속 누른다.
    time.sleep(0.1) #너무빨리 누르면 인식 못할 수 있으니 기다려주자.

try:
    driver.find_element(By.CSS_SELECTOR,'#islmp > div > div > div > div > div.gBPM8 > div.qvfT1 > div.YstHxe > input').click() #계속 내리다보면 결과 더보기가 뜨는데 그거 찾는것.
    
    for i in range(60): #다시 60번 페이지다운
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
except:
    pass


# In[43]:


links = [] #사진 링크들 저장할 리스트
images = driver.find_elements(By.CSS_SELECTOR, '#islrg > div.islrc > div > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img') #f12눌러 사진 선택해서 링크 
#2가지 사진 링크
# #islrg > div.islrc > div:nth-child(403) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img
# #islrg > div.islrc > div:nth-child(408) > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img
#가운데 숫자만 다르다.
# #islrg > div.islrc > div > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img로 하면 됨.


for image in images:
    if image.get_attribute('src') is not None: #src는 source다. 데이터가 없지 않으면 계속 데이터 links에 추가해준다.
        links.append(image.get_attribute('src'))

print("찾은 이미지 개수:", len(links)) #찾은 이미지 개수 출력


# In[44]:


#자동 다운

import urllib.request

for k, i in enumerate(links):
    url = i
    urllib.request.urlretrieve(url, "C:\\Users\\User\\Desktop\\python\\40 Python works\\3. Project\\2. Google Image Crawling\\"
    + str(k) + '.jpg') #절대경로로 해야댐. 상대경로 안돼!

print("다운로드 완료되었습니다.")

