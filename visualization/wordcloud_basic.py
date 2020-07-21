# %% [markdown]
# 워드클라우드 만들기
# %%
f = open("토지1.txt", "r", encoding="cp949")
story = f.read()
f.close()


# %%
print(type(story))
print(story)


# %%
from wordcloud import WordCloud
import matplotlib.pyplot as plt


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
stopwords_kr = ["있었다", "것이다"]

displayWordCloud(story)

# %%
from soynlp.noun import NewsNounExtractor

noun_extractor = NewsNounExtractor()
nouns = noun_extractor.train_extract(story.split(" "))  # list of str like
displayWordCloud(" ".join(nouns))

# %%
from konlpy.tag import Kkma
from konlpy.utils import pprint

# %%
kkma = Kkma()
print(kkma.nouns(u"대학에서 DB, 통계학, 이산수학 등을 배웠지만..."))

# %%
from konlpy.tag import Okt

okt = Okt()
nouns = okt.nouns(story)
# displayWordCloud(" ".join(nouns))


# %%
from PIL import Image
import numpy as np

img = Image.open("cloud.png")
img_arr = np.array(img)
img_arr

# %%
wordcloud = WordCloud(
    font_path="C:\\Users\\admin\\AppData\\Local\\Microsoft\\Windows\\Fonts\\NanumBarunGothic.ttf",
    background_color="white",
    width=800,
    height=600,
    mask=img_arr,
).generate(" ".join(nouns))
plt.figure(figsize=(15, 10))
plt.imshow(wordcloud)
plt.axis("off")
wordcloud.to_file("cloud.png")

# %%
