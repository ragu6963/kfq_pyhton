from bs4 import BeautifulSoup
from selenium import webdriver
import time, requests

driver = webdriver.Chrome("./kfq_python/crawling/data/chromedriver")
driver.get("https://www.starbucks.co.kr/store/store_map.do")
time.sleep(7)

# 현 위치 기준 매장 이름
source = driver.page_source
st_bs = BeautifulSoup(source, "html.parser")
st_bs = st_bs.select("li.quickResultLstCon")
for st in st_bs:
    print(st.select_one("strong").get_text())
    print(st["data-lat"])
    print(st["data-lng"])
    print("-----------------")

