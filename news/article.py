# 2023년 8월 한달동안의 연합뉴스 크롤링 (날짜,타이틀,기사본문,기사반응,카테고리), 본문 전처리 진행
import requests
import csv
from bs4 import BeautifulSoup

#날짜, 타이틀, 기사본문, 카테고리 가져오기
URL = "https://n.news.naver.com/mnews/article/001/0014164627"
h = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}

res = requests.get(URL, headers=h)
bs = BeautifulSoup(res.text, 'html.parser')

print(bs.select_one('span').attrs['data-date-time'])# 날짜

bs.select_one('#title_area').text #타이틀
bs.select_one('') #기사본문
#카테고리