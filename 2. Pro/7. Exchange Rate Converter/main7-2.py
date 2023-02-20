#최근 우리나라 환율 조회. 실시간은 아님.
from currency_converter import CurrencyConverter

cc = CurrencyConverter('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip') # ZIP파일을 다운받아 최신의 환율이 적용됨. 하루에 한번만 다운해주자.
print(cc.convert(1, 'USD', 'KRW')) #1달러당 원화 비율