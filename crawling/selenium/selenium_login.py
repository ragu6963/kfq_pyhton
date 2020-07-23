id = "네이버아이디"
pw = "네이버패스워드"


from bs4 import BeautifulSoup
from selenium import webdriver
import time, requests
import pyperclip
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def copy_input(xpath, input):
    pyperclip.copy(input)
    driver.find_element_by_xpath(xpath).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").key_up(
        Keys.CONTROL
    ).perform()
    time.sleep(1)


driver = webdriver.Chrome("./kfq_python/crawling/data/chromedriver")
driver.get("https://nid.naver.com/nidlogin.login")
driver.implicitly_wait(3)

# 로그인 방법 1 COPY & PASTE
# copy_input('//*[@id="id"]', id)
# copy_input('//*[@id="pw"]', pw)

# 로그인 방법 2 Script 이용
driver.execute_script("document.getElementsByName('id')[0].value='" + id + "'")
driver.execute_script("document.getElementsByName('pw')[0].value='" + pw + "'")
time.sleep(1)

# xpath 이용
driver.find_element_by_xpath('//*[@id="log.login"]').click()
time.sleep(1)

# id 이용 셀렉터

# driver.find_element_by_id("log.login").click()

# 네이버 메일 페이지 크롤링
driver.get("https://mail.naver.com/")
driver.implicitly_wait(3)
source = driver.page_source
soup = BeautifulSoup(source, "html.parser")
mail_list = soup.select("ol.mailList > li > div.mTitle")
for mail in mail_list:
    mail_title = mail.select_one("strong")
    print(mail_title.get_text())


# 네이버 메인 페이지 - 마이페이지 IFRAME 처리
# # -----------------------------
# iframe_id = "minime"
# source = driver.page_source
# time.sleep(2)

# iframe = driver.find_element_by_id(iframe_id)
# driver.switch_to_frame(iframe)


# # 네이버 메일 정보
# driver.find_element_by_xpath('//*[@id="NM_MY_TAB"]/div/div[1]/a[3]').click()
# source = driver.page_source
# time.sleep(1)

# # 전체 정보
# mail_list = driver.find_elements_by_css_selector(
#     "body > div > div > div.sc_service > div.service_wrap.MY_SERVICE > div.service_body > div > ul >li"
# )

# for mail in mail_list:
#     mail_title = mail.find_element_by_css_selector("em.title")
#     print(mail_title.text)

# # 첫번째 메일 정보
# # mail_title = driver.find_element_by_xpath(
# #     "/html/body/div/div/div[2]/div[1]/div[2]/div/ul/li[1]/div/a[1]/div[1]/em"
# # ).text
# # print(mail_title)

# #  네이버 페이 정보
# driver.find_element_by_xpath('//*[@id="NM_MY_TAB_next"]').click()
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="NM_MY_TAB"]/div/div[2]/a[1]').click()
# time.sleep(1)

# pay_money = driver.find_element_by_xpath(
#     "/html/body/div/div/div[2]/div[1]/div/div[1]/ul/li[1]/a/strong"
# ).text
# print("페이 머니 :", pay_money)
