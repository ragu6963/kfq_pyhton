# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색

import urllib.request
import json
from operator import itemgetter


client_id = "YOUR_CLIENT_ID"
client_secret = "YOUR_CLIENT_SECRET"
encText = urllib.parse.quote("통밀빵")
result_list = []
for i in range(1, 1000, 100):
    url = (
        "https://openapi.naver.com/v1/search/shop.json?query="
        + encText
        + "&display=100"
        + "&start="
        + str(i)
    )  # json 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",)
    request.add_header("X-Naver-Client-Secret",)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
        json_data = response_body.decode("utf-8")
        dic = json.loads(json_data)
        dic = dic["items"]
        for item in dic:
            title = item["title"].replace("<b>", "").replace("</b>", "")
            lprice = item["lprice"].replace("<b>", "").replace("</b>", "")
            link = item["link"].replace("<b>", "").replace("</b>", "")

            result = {}
            result["title"] = title
            result["lprice"] = lprice
            result["link"] = link
            result_list.append(result)

            # print("제목 : %s" % title)
            # print("최저가 : %s" % lprice)
            # print("링크 : %s" % link)
            # print(
            #     "------------------------------------------------------------------------------------------------"
            # )

    else:
        print("Error Code:" + rescode)

data = sorted(result_list, key=itemgetter("lprice"), reverse=True)
for item in data:
    print(item)

