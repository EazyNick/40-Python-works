#내가 따로 또 사용하는 IP가 있는지 확인, 가상환경, 서버 등
import socket
in_addr = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #AF_INET은 요즘 집주소를 규정하는 방식이다. socket.SOCK_STREAM은 TCP/IP를 사용하겠다는 뜻
in_addr.connect(("www.google.co.kr",443)) #433은 https의 일반적인 주소채널
print(in_addr.getsockname()[0]) #구글에 들어가 내 IP확인. 가상환경을 사용중이라면 이방법으로 확인 가능.