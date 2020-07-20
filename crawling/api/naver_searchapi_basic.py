# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색

import os
import sys
import urllib.request
import json
 
encText = urllib.parse.quote("오마이걸 아린")
for i in range(1, 1000, 100):
    url = (
        "https://openapi.naver.com/v1/search/news.json?query="
        + encText
        + "&display=100"
        + "&sort=date"
        + "&start="
        + str(i)
    )  # json 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", )
    request.add_header("X-Naver-Client-Secret", )
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
        json_data = response_body.decode("utf-8")
        dic = json.loads(json_data)
        dic = dic["items"]
        for item in dic:
            title = item["title"].replace("<b>", "").replace("</b>", "")
            description = item["description"].replace("<b>", "").replace("</b>", "")

            TODO:# postdata == blog 날짜
            # postdate = item["postdate"].replace("<b>", "").replace("</b>", "")

            TODO:# pubDate == news 날짜
            pubDate = item["pubDate"].replace("<b>", "").replace("</b>", "")

            print("제목 : %s" % title)
            # print("날짜 : %s" % postdate)
            print("날짜 : %s" % pubDate)
            print("내용\n%s" % description)
            print(
                "------------------------------------------------------------------------------------------------"
            )

    else:
        print("Error Code:" + rescode)
