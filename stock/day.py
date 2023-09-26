import requests
from bs4 import BeautifulSoup

URL = "https://finance.naver.com/item/sise.nhn?code=005930"
res = requests.get(URL)
bs = BeautifulSoup(res.text, "html.parser")

#일별 시세 사이트 들어가기
print(bs.select_one("iframe").attrs["src"])