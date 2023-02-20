#영어로된 파일을 읽어 한글로 번역하고 새로운 파일로 저장하는 프로그램 만들기.
#pip install googletrans==4.0.0-rc1 구글 번역기 사용
#구글 번역.
import googletrans

translator = googletrans.Translator()

str1 = "행복하세요"
result1 = translator.translate(str1, dest='en', src='auto') #str1을 목적지(dest)로, 소스는 자동으로
print(f"행복하세요 => {result1.text}")

str2 = "I am happy"
result2 = translator.translate(str2, dest='ko', src='en') #str2를 목적지(한국어)로, 소스는 영어이다.
print(f"I am happy => {result2.text}")