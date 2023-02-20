from ppadb.client import Client
import time

def adb_connect(): #함수하나 만듬
    client = Client(host='127.0.0.1',port=5037)
    find_devices = client.devices()

    if len(find_devices) == 0:
        print("No devices")
        quit()

    device = find_devices[0] #찾은 디바이스 첫번쨰것을 device변수로 지정
    print(f'찾은 디바이스{device}')

    return device, client

device, client = adb_connect()

device.shell('input keyevent 64') 
time.sleep(3.0)

xyPosition = '423 136'
device.shell(f'input tap {xyPosition}') #클릭
time.sleep(2.0)

url = 'www.naver.com'
device.shell(f'input text {url}') #클릭
time.sleep(2.0)

device.shell('input keyevent 66') #클릭
time.sleep(2.0)

result = device.screencap() #캡처
with open(r'40 Python works\3. Project\Smartphone automation\screen.png', 'wb') as fp: #파일 저장
    fp.write(result) #write는 파일에 뭔가를 적을때 사용
#wb는 쓰기모드로 바이너리(2진법) 모드로 열겠다는 것. 사진이기때문에 wb사용