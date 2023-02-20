#쉬운 웹앱만들기 html안쓰고 라이브러리 이용해 파이썬으로 쉽게 제작.
#streamlit, pyupbit pip install 해주기
#pyupbit는업비트에서 가상화폐 데이터 조회할 수 있는 라이브러리임.
#가상화폐 시세 조회해서 가격 출력하는 웹앱 만들어보자.
#4. Creating... 폴더로 통합 터미널 열고 streamlit run main4-1.py 입력하기. 
#이메일 입력해주기.

import streamlit as st

data_list = {1,2,3,4,5,6,7,8,9,10}
st.write('''
샘플데이터
''') #글씨 작성

st.line_chart(data_list) #차트그리기