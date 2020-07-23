# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython
from numpy.core.fromnumeric import sort

# %%
get_ipython().run_line_magic("matplotlib", "inline")
import urllib.request
import json, datetime, time
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import warnings

warnings.filterwarnings("ignore")
key = ""

# %%
# 일별 박스오피스
def cineBoxInfo():
    # 오늘 날짜를 가져와서 사용할 형식으로 만든다.
    movieDate = time.strftime("%Y%m%d", time.localtime(time.time()))

    cine = []
    for i in range(0, 30):
        # 자료는 매일 갱신되며 갱신 시간이전에 요청시 내용이 비어 있음.
        # 반복 함수 마지막에 날짜를 줄이는 함수를 사용한다.
        # str -> date
        datetime_obj = datetime.datetime.strptime(movieDate, "%Y%m%d").date()

        # 1일 혹은 1주일씩 시간을 줄여간다.
        datetime_obj_tmp = datetime_obj - datetime.timedelta(days=1)  # weeks=1

        # date -> str
        movieDate = datetime_obj_tmp.strftime("%Y%m%d")
        print(movieDate, end=" ")

        url = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={key}&targetDt={movieDate}"
        response = urllib.request.urlopen(url)
        # print(response)

        rescode = response.getcode()

        if rescode == 200:
            responseData = response.read()

        result = json.loads(responseData)
        # print(result)
        pre_result = result["boxOfficeResult"]["dailyBoxOfficeList"]
        # print(pre_result)

        for i in range(0, len(pre_result)):
            pre_result[i]["targetDt"] = movieDate
            cine.append(pre_result[i])

    print()
    # list->dataframe
    dataframe = pd.DataFrame(cine)
    print(dataframe.columns)
    dataframe.to_csv("cinebox.csv", index=False)
    return dataframe


# %%
# 영화상세정보
def cineInfo(movieCd):
    url = (
        f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd="
        + str(movieCd)
    )
    response = urllib.request.urlopen(url)
    text = response.read()
    # print(text)
    d = json.loads(text)
    # print(d)
    movieInfo = d["movieInfoResult"]["movieInfo"]
    return movieInfo


# %%
cineBoxInfo()


# %%
# 영화코드를 인자로 받아 영화상세정보 리턴
movieInfo = cineInfo(20193450)
movieInfo


# %%
print(
    movieInfo["movieCd"],
    movieInfo["movieNm"],
    movieInfo["showTm"],
    len(movieInfo["actors"]),
    len(movieInfo["showTypes"]),
)


# %%
# 필요한 영화 코드
df = pd.read_csv(r"cinebox.csv", engine="python", encoding="utf-8")
df


# %%
codeitem = pd.unique(df["movieCd"])
codeitem.tolist()
print(codeitem)

cine = []
for code in codeitem:
    movieInfo = cineInfo(code)
    item = {
        "movieCd": movieInfo["movieCd"],
        "movieNm": movieInfo["movieNm"],
        "showTm": movieInfo["showTm"],
        "actors": len(movieInfo["actors"]),
        "showTypes": len(movieInfo["showTypes"]),
    }
    cine.append(item)

dataframe = pd.DataFrame(cine)
dataframe.to_csv("cine.csv", index=False)


# %%
def graph_m(title):
    df = pd.read_csv(r"cinebox.csv", engine="python", encoding="utf-8")
    # print(df.head())
    # print("-" * 60)
    # df=df.drop('Unnamed: 0',axis=1)  # 불러온 컬럼중 제거할 컬럼이 있다면 제거한다.
    df.drop("rnum", axis=1, inplace=True)
    # print(df.head())
    # print(df.columns)
    temp = df[df["movieNm"] == title]
    # print(temp[["salesAmt", "targetDt", "movieNm"]])
    temp = temp.sort_values(by="targetDt")
    # print(temp.dtypes)
    mpl.rc("font", family="NanumBarunGothic")  # 한글 폰트 설정
    plt.bar(temp["targetDt"].astype(str), temp["salesAmt"])
    plt.title("일별 매출액 막대 그래프")
    plt.xlabel("날짜")
    plt.ylabel("총매출액")
    plt.xticks(fontsize=10, rotation=90)
    url1 = "" + title + ".png"
    plt.savefig(url1)


# %%
graph_m("반도")


# %%
df = pd.read_csv(r"cinebox.csv", engine="python", encoding="utf-8")
df.head()


# %%
df["movieNm"] == "반도"


# %%
temp1 = df[df["movieNm"] == "반도"]
temp1.head()


# %%

mpl.rc("font", family="NanumBarunGothic")  # 한글 폰트 설정
plt.plot([str(x) for x in temp1["targetDt"]], temp1["salesAmt"])
plt.title('"{}"의 일별 매출액(salesAmt) 선 그래프'.format(temp1.iloc[0, 5]))
plt.xlabel("날짜")
plt.ylabel("매출액")
plt.xticks(fontsize=9, rotation=90)
plt.show()


# %%
temp1.iloc[0, 5]


# %%
temp = df.groupby("movieNm").sum()
temp

# %%
temp = df.groupby("movieNm").count()
temp


# %%
mpl.rc("font", family="NanumBarunGothic")  # 한글 폰트 설정
plt.figure(figsize=(15, 5))
plt.bar(temp.index, temp["salesAmt"])
plt.title("영화명(movieNm)별 총 매출액 막대 그래프")
plt.xlabel("영화명")
plt.ylabel("총매출액")
plt.xticks(fontsize=9, rotation=90)
plt.show()

# %% [markdown]
# - 분포도 그리기

# %%
df = pd.read_csv(r"cinebox.csv", engine="python", encoding="utf-8")
temp = df.groupby("movieNm").sum()
temp.head()


# %%
mpl.rc("font", family="NanumBarunGothic")  # 한글 폰트 설정
plt.figure(figsize=(10, 5))
# plt.scatter(temp['salesAmt'], temp['audiCnt'])
plt.scatter(temp["salesAmt"], temp["audiCnt"])
plt.title("총 매출액과 총 관객수 분포도")
plt.xlabel("총매출액")
plt.ylabel("총관객수")
plt.show()

# %% [markdown]
# - 파이차트 그리기

# %%
df = pd.read_csv(r"cinebox.csv", engine="python", encoding="utf-8")
temp = df.groupby("movieNm").sum()
temp = temp.sort_values(by="salesAmt", ascending=0)
temp = temp.iloc[:10]
temp


# %%
mpl.rc("font", family="NanumBarunGothic")  # 한글 폰트 설정
mpl.rcParams["font.size"] = 9
plt.figure(figsize=(10, 5))
plt.pie(temp["salesAmt"], labels=temp.index, autopct="%.1f%%", shadow=True)
plt.title("총 매출액 TOP 10 의 영화명(movieNm) 파이 차트")
plt.show()


# %%
df1 = pd.read_csv(r"cinebox.csv", engine="python", encoding="utf-8")
df1


# %%
df2 = pd.read_csv(r"cine.csv", engine="python", encoding="utf-8")
df2


# %%
df3 = pd.merge(df1, df2, on="movieCd")
df3


# %%
df3["rankOldAndNew"].replace(["OLD", "NEW"], [0, 1], inplace=True)
# df3=df3['rankOldAndNew'].replace(['OLD','NEW'],[0,1])


# %%
df3


# %%
df3 = df3.loc[
    :,
    [
        "targetDt",
        "rank",
        "rankOldAndNew",
        "movieCd",
        "salesAmt",
        "audiCnt",
        "showTm",
        "actors",
        "showTypes",
    ],
]
df3


# %%
# 상관계수 두 변수간의 연관된 정도를 나타낸다. 두변수가 동일하면 +1, 전혀 다르면 0, 반대방향으로 동일하면 -1
temp = df3.corr()
temp


# %%
temp = temp.rename(
    index={
        "targetDt": "날짜",
        "rank": "순위",
        "rankOldAndNew": "신규진입여부",
        "movieCd": "영화코드",
        "salesAmt": "매출액",
        "audiCnt": "관객수",
        "showTm": "상영시간",
        "actors": "배우 수",
        "showTypes": "상영형태 수",
    }
)
temp = temp.rename(
    columns={
        "targetDt": "날짜",
        "rank": "순위",
        "rankOldAndNew": "신규진입여부",
        "movieCd": "영화코드",
        "salesAmt": "매출액",
        "audiCnt": "관객수",
        "showTm": "상영시간",
        "actors": "배우 수",
        "showTypes": "상영형태 수",
    }
)
temp


# %%
mpl.rc("font", family="NanumBarunGothic")  # 한글 폰트 설정
plt.figure(figsize=(10, 10))
plt.imshow(temp, cmap="hot")
plt.colorbar()
plt.title("영화 박스오피스의 컬럼들간의 상관계수 히트맵")
# plt.xticks(range(9), ['targetDt','rank','rankOldAndNew','movieCd','salesAmt','audiCnt','showTm','actors','showTypes'])
plt.xticks(range(len(temp.columns)), temp.columns)
plt.xticks(fontsize=10, rotation=45)
plt.yticks(range(len(temp.index)), temp.index)
plt.yticks(fontsize=10, rotation=45)
plt.show()


# %%
df = pd.read_csv(r"cinebox.csv", engine="python", encoding="utf-8")
df.head()


# %%
temp1 = df[df["movieNm"] == "반도"]
temp1.head()


# %%
temp2 = df[df["movieNm"] == "#살아있다"]
temp2.head()


# %%
mpl.rc("font", family="NanumBarunGothic")  # 한글 폰트 설정
fig = plt.figure()
fig.set_size_inches(12, 5)

# 분할해 그리기 시작
axe = fig.add_subplot(1, 2, 1)  # 1행(row) 2열(column)중 첫 번째 subplot
axe.plot([str(x) for x in temp1["targetDt"]], temp1["salesAmt"])
axe.set_title("반도")
axe.set_xlabel("날짜")
axe.set_ylabel("매출액")
for tick in axe.xaxis.get_major_ticks():
    tick.label.set_fontsize(9)
    tick.label.set_rotation(90)

axe = fig.add_subplot(1, 2, 2)  # 1행(row) 2열(column)중 두번째 subplot
axe.plot([str(x) for x in temp2["targetDt"]], temp2["salesAmt"])
axe.set_title("#살아있다")
axe.set_xlabel("날짜")
axe.set_ylabel("매출액")
for tick in axe.xaxis.get_major_ticks():
    tick.label.set_fontsize(9)
    tick.label.set_rotation(90)
plt.suptitle('영화명 "인비저블맨"의 일별 매출액(salesAmt)과 영화명 "1917"의 일별 매출액(salesAmt) 선 그래프')
# 분할해 그리기 끝
plt.show()


# %%
df = pd.read_csv(r"cinebox.csv", engine="python", encoding="utf-8")
df.head()


# %%
temp1 = df[df["movieNm"] == "반도"]
temp1.head()


# %%
temp2 = df[df["movieNm"] == "#살아있다"]
temp2.head()


# %%
dates = list(set(temp1["targetDt"]) | set(temp2["targetDt"]))
dates.sort()
len(dates)


# %%
def apply_temp1(date):
    return dates.index(date)


temp1["x"] = temp1["targetDt"].apply(apply_temp1)
temp1


# %%
def apply_temp2(date):
    return dates.index(date)


temp2["x"] = temp2["targetDt"].apply(apply_temp2)
temp2.head()


# %%
mpl.rc("font", family="NanumBarunGothic")  # 한글 폰트 설정
plt.plot(temp1["x"], temp1["salesAmt"], label="반도")
plt.plot(temp2["x"], temp2["salesAmt"], label="#살아있다")
plt.title('영화명 "반도"의 일별 매출액(salesAmt)과 영화명 "#살아있다"의 일별 매출액(salesAmt) 선 그래프')
plt.xlabel("날짜")
plt.ylabel("매출액")
plt.xticks(range(len(dates)), dates, fontsize=6, rotation=90)
plt.legend(loc=1)  # 범례
plt.show()


# %%
