import requests
import csv
from bs4 import BeautifulSoup

file = open("stock.csv", mode="w", encoding="utf-8", newline="")
writer = csv.writer(file)

h = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"}
URL = "https://finance.naver.com//item/sise_day.naver"

for page in range(2,5):

    params = {'code':'005930', 'page':page}
    
    res = requests.get(URL, params = params, headers=h)
    bs = BeautifulSoup(res.text, "html.parser")


    for data in bs.select(".type2 tr") :
        if len(data.select("td")) == 7 :
            writer.writerow([data.select("td")[0].text.replace(".","-")
                             , data.select("td")[1].text.replace(",","")])
file.close()