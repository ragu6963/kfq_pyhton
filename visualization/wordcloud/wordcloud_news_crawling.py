# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

news = []
url = "https://news.naver.com/"
response = urllib.request.urlopen(url)
soup = BeautifulSoup(response, "html.parser")
results = soup.select(".section_list_ranking li a")
for result in results:
    # print('제목:',result.attrs['title'])
    # print('링크:',result.attrs['href'])
    title = result.attrs["title"]
    href = result.attrs["href"]
    url_content = "https://news.naver.com" + result.attrs["href"]
    response_content = urllib.request.urlopen(url_content)
    soup_content = BeautifulSoup(response_content, "html.parser")
    content = soup_content.select_one("#articleBodyContents")
    # print(content.contents)

    # 가공작업
    output = ""
    for item in content.strings:
        stripped = str(item).strip()  # 공백제거
        if stripped == "":
            continue
        else:
            output += item
    output = output.replace("본문 내용TV플레이어", "")
    output = output.replace("// flash 오류를 우회하기 위한 함수 추가", "")
    output = output.replace("function _flash_removeCallback() {}", "")
    output = output.strip()
    news.append({"title": title, "href": href, "contents": output})

# print(news)
dataframe = pd.DataFrame(news)
dataframe.to_csv("news.csv", index=False)


# %%
import pandas as pd

df = pd.read_csv("news.csv", engine="python", encoding="utf-8")


# %%
sample_title = df["title"][:2]
sample_title

# %%
sample_contents = df["contents"][:2]
sample_contents


# %%
# 관심 주제 설정
import re

# 정규식으로 단어가 들어간 문장만 필터
p = ".*(코로나|여행|비행|호텔).*"
topic = df[df["title"].str.match(p) | df["contents"].str.match(p)]
topic.shape


# %%
topic.head()


# %%
# %%
from wordcloud import WordCloud
import matplotlib.pyplot as plt

stopwords_kr = [
    "기자",
    "사람",
    "배포 금지",
    "무단 배포",
    "지난",
    "사진",
    "대한",
    "제품",
    "이번",
    "시간",
    "때문",
    "대해",
    "경우",
    "위해",
    "사실",
    "통해",
    "연합뉴스",
    "뉴스",
    "배포",
    "금지",
    "무단",
    "실제",
]


def displayWordCloud(data=None, backgroundcolor="white", width=800, height=600):
    wordcloud = WordCloud(
        font_path="C:\\Users\\admin\\AppData\\Local\\Microsoft\\Windows\\Fonts\\NanumBarunGothic.ttf",
        background_color=backgroundcolor,
        width=width,
        height=height,
        stopwords=stopwords_kr,
    ).generate(data)
    print(wordcloud.words_)
    plt.figure(figsize=(15, 10))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()


# %%
from konlpy.tag import Kkma

kkma = Kkma()
nouns = kkma.nouns(" ".join(df["contents"]))
displayWordCloud(" ".join(nouns))


# %%
from soynlp.noun import NewsNounExtractor

noun_extractor = NewsNounExtractor()
nouns = noun_extractor.train_extract(df["contents"])  # list of str like
displayWordCloud(" ".join(nouns))


# %%
