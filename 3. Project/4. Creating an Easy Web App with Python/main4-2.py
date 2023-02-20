#날짜 출력

import streamlit as st
import datetime

#날짜 입력 위젯을 표시합니다
d = st.date_input(
    "날짜를 선택하세요",
    datetime.date.today()) #오늘날짜로 출력.

st.write('선택한 날짜:',d)