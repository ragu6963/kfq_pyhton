# %%
from key import Key

key = Key()._getkey()
# %% [markdown]
# curl -v -X GET "https://dapi.kakao.com/v2/local/search/address.json" \
# --data-urlencode "query=전북 삼성동 100" \
# -H "Authorization: KakaoAK kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"

# %%
import requests
import json

# %%
url = """
https://dapi.kakao.com/v2/local/search/address.json?query=경산 둥지로 11길 7-4
"""
headers = {"Authorization": f"KakaoAK {key}"}
res = requests.get(url, headers=headers)
response_body = res.json()
print(response_body["documents"][0]["address"]["address_name"])

# %%
url = """
https://dapi.kakao.com/v2/local/search/address.json?query=대구 서구 비산6동 385-3
"""
headers = {"Authorization": f"KakaoAK {key}"}
res = requests.get(url, headers=headers)
print(res.text)


# %%
x = 127.1086228
y = 37.4012191
url = f"""
https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x={x}&y={y}
"""
headers = {"Authorization": f"KakaoAK {key}"}
res = requests.get(url, headers=headers)
print(res.text)


# %%
x = 127.06283102249932
y = 37.514322572335935
radius = 20000
query = "카카오프렌즈"
url = f"""
https://dapi.kakao.com/v2/local/search/keyword.json?y={y}&x={x}&radius={radius}&query={query}
"""
headers = {"Authorization": f"KakaoAK {key}"}
res = requests.get(url, headers=headers)
print(res.text)


# %%
query = "대구시청"
category_group_code = "PO3"
url = f"""
https://dapi.kakao.com/v2/local/search/keyword.json?query={query}&category_group_code={category_group_code}
"""
headers = {"Authorization": f"KakaoAK {key}"}
res = requests.get(url, headers=headers)
res.json()


# %%
query = "대구비즈니스센터"
url = f"""
https://dapi.kakao.com/v2/local/search/keyword.json?query={query}
"""
headers = {"Authorization": f"KakaoAK {key}"}
res = requests.get(url, headers=headers)
res.json()


# %%
query = "대구비즈니스센터"
x = 128.506658596964
y = 35.8364571177044
category_group_code = "CS2"
radius = 2000
url = f"""
https://dapi.kakao.com/v2/local/search/category.json?x={x}&y={y}&category_group_code={category_group_code}&radius={radius}
"""
headers = {"Authorization": f"KakaoAK {key}"}
res = requests.get(url, headers=headers)
res.json()


# %%
