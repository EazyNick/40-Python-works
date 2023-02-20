#환율 변환기, pip install currencyconverter로 해야댐. 
from currency_converter import CurrencyConverter

cc = CurrencyConverter() #어떤 통화를 환율로 변환할 수 있는지 확인. 한국은 KRW
print(cc.currencies) 
