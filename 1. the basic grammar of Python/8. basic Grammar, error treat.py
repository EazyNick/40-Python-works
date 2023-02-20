#기본 문법과 오류 및 예외처리 try: except: 사용
#에러가 나면 시스템이 멈추기에, 예외처리를 해줘야함.
try:
    dklashsadwq
except:
    pass #에러가나면 아무것도 하지않고 싶을때 pass
print("에러발생")

try:
    ㅇ1231234121
except Exception as e: #에러 발생 원인 알수있음.
    print("에러발생원인:", e)