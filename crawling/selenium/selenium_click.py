from bs4 import BeautifulSoup
from selenium import webdriver
import time, requests

driver = webdriver.Chrome("./kfq_python/crawling/data/chromedriver")
driver.get("https://www.starbucks.co.kr/store/store_map.do")
time.sleep(10)

# 현 위치 기준 매장 이름
source = driver.page_source
st_bs = BeautifulSoup(source, "html.parser")

loca_btn = driver.find_element_by_class_name("loca_search")
loca_btn.click()
loca = driver.find_element_by_class_name("sido_arae_box")
li = loca.find_elements_by_tag_name("li")
li[3].click()
time.sleep(10)

ul = driver.find_element_by_class_name("gugun_arae_box")
li = ul.find_elements_by_tag_name("li")
li[0].click()
time.sleep(10)


source = driver.page_source
st_bs = BeautifulSoup(source, "html.parser")
st_bs = st_bs.select("ul.quickSearchResultBoxSidoGugun > li.quickResultLstCon")
for st in st_bs:
    print("매장 이름 :", st.select_one("strong").get_text())
    print("매장 주소 :", st.select_one(".result_details").get_text())
    print(st["data-lat"])
    print(st["data-long"])
    print("-----------------")
