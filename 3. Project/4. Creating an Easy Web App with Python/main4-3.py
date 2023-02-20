import streamlit as st
import datetime
import pyupbit

d = st.date_input(
    "날짜를 선택하세요",
    datetime.date.today())

st.write('비트코인 1일 차트')

ticker = 'KRW-BTC'
interval = 'minute60'
to = str(d + datetime.timedelta(days=1)) #d(내가 선택한 날짜에 + 날짜 +1해주겠다.)
count = 24
price_now = pyupbit.get_ohlcv(ticker, interval=interval, to=to, count=count) # interval = 60분봉 데이터, to=설정 기간의 60분 이전의 데이터를 200개조회
#200개 조회하는게 get_ohlcv함수임. count(24개)만큼의 이전 영업일까지 조회합니다.
st.line_chart(price_now.close)