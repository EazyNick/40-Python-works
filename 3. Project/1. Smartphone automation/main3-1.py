#안드로이드 스마트폰 자동화 프로그램 만들기
#구글 adb이용, 컴퓨터로 하기위해 블루스택 사용.
#platform-tools를 마우스 우클릭 후 통합 터미널에서 열기하면 platform-tools경로의 터미널이 하나 열린다.
#입력에 .\adb start-server입력
#adb서버가 열려 블루스택과 통신할 준비가 되어있다.
#pip install pure-pyp install pure-python-adb

from ppadb.client import Client

client = Client(host='127.0.0.1',port=5037)
find_devices = client.devices()

if len(find_devices) == 0:
    print("No devices")
    quit()

device = find_devices[0]
print(f'찾은 디바이스{device}')

#찾으면 디바이스의(객체의) 주소가 출력됨. 못찾으면 중지.