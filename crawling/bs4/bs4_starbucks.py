from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

url = "https://www.starbucks.co.kr/store/store_map.do"
with urllib.request.urlopen(url) as response:
    html = response.read()
    soup = BeautifulSoup(html, "html.parser")
result_list = soup.select("li.quickResultLstCon")
for result in result_list:
    print(result)

