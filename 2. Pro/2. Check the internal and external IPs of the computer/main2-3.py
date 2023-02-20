#외부 IP는 내가 확인 불가능하고 따로 사이트 들어가서 확인해야함. 난왜 외부, 내부IP가 똑같냐..
import requests #어딘가에 접속할떄 사용
import re #문자의 특정 패턴을 파악해서 문자를 분리하는 기능

req = requests.get("http://ipconfig.kr")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1]

print(out_addr)

#print(req.text) #사이트 접속 후 사이트 코딩된 것 작성해줌.