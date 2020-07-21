import urllib.request
import json
import datetime

key = ""
main_url = (
    "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
)
now = datetime.datetime.now()

for i in range(1, 30):
    dt = now - datetime.timedelta(days=int(i))
    dt = dt.strftime("%Y%m%d")
    print(dt)
    url = main_url + f"?key={key}&targetDt={dt}"

    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if rescode == 200:
        response_body = response.read()
        json_data = response_body.decode("utf-8")
        json_data = json.loads(json_data)
        boxOfficeResult = json_data["boxOfficeResult"]
        dailyBoxOfficeList = boxOfficeResult["dailyBoxOfficeList"]
        for item in dailyBoxOfficeList:
            print(f"{item['rank']:>2}. {item['movieNm']}")
    else:
        print("Error Code:" + rescode)
