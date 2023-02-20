from ppadb.client import Client
import time

def adb_connect(): #함수하나 만듬
    client = Client(host='127.0.0.1',port=5037)
    find_devices = client.devices()

    if len(find_devices) == 0:
        print("No devices")
        quit()

    device = find_devices[0]
    print(f'찾은 디바이스{device}')

    return device, client

device, client = adb_connect()
#컴퓨터와 디바이스를 연결!

device.shell('input keyevent 64') #64라는게 기본 웹브라우저를 열라는 명령.
time.sleep(3.0)
