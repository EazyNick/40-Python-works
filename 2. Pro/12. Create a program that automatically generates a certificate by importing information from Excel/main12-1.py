#엑셀에 저장된 수료증 명단 정보를 불러와 워드로 수료증을 자동생성 하고 PDF로 변환하는 프로그램
#openpyxl은 엑셀을 사용하기 위한 라이브러리
#python-docx는 워드를 사용하기 위한 라이브러리
#docx2pdf는 워드를 pdf로 변환할 때 사용하는 라이브러리
#엑셀이 없다면 판다스 사용 유명해! 엄청난 양의 데이터를 만들때만 유용, 나머진 그냥 엑셀 써..
#판다스로 데이터 만들어 엑셀로 저장하기

import pandas as pd

df = pd.DataFrame([["홍길동", "1990.01.02", "2021-0001"],
                    ["김민준", "1990.05.06", "2021-0002"],
                    ["김철수", "2000.08.08", "2021-0003"],
                    ["김영희", "1990.09.09", "2021-0004"],
                    ["이서준", "2010.10.10", "2021-0005"],
                    ["장다인", "2017.12.12", "2021-0006"]])

print(df)
df.to_excel(r'40 Python works\Create a program that automatically generates a certificate by importing information from Excel\수료증명단.xlsx', index=False, header=False)
