#%%
import folium
import pandas as pd
import requests
import json
import webbrowser


# %%
filename = "jeju.csv"
df = pd.read_csv(filename, encoding="cp949", header=0)
address = df["주소"]
# %%
for add in address:
    print(add)


# %%
from key import Key

key = Key()._getkey()


# %%
address_dict = {}

for add in address:
    add = add.split("(")[0]
    url = f"""
    https://dapi.kakao.com/v2/local/search/address.json?query={add}
    """
    headers = {"Authorization": f"KakaoAK {key}"}
    res = requests.get(url, headers=headers)
    data = res.json()["documents"][0]["address"]
    address_name = data["address_name"]
    address_dict[add] = {"x": data["x"], "y": data["y"]}


# %%
for k, v in address_dict.items():
    print(k, v)


# %%
hanla = [33.3616649, 126.511657]
map_osm = folium.Map(location=[hanla[0], hanla[1]], zoom_start=9)
for name, loca in address_dict.items():
    folium.Marker([loca["y"], loca["x"]], popup=name).add_to(map_osm)
map_osm
# map_osm.save("map.html")
# %%


# %%
