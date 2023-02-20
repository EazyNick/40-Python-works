# 내부 IP출력, 공유기에서 할당해준 IP주소이다.
import socket 
in_addr = socket.gethostbyname(socket.gethostname())
print(in_addr)
