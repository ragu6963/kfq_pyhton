# %%
import folium
import json

map_osm = folium.Map(location=[37.566345, 126.977893])
rfile = open(
    "./folium_json/skorea-provinces-2018-geo.json", "r", encoding="utf-8",
).read()
jsonData = json.loads(rfile)
folium.GeoJson(jsonData, name="json_data").add_to(map_osm)
map_osm

# %%
map_osm = folium.Map(
    location=[33.50704277172384, 126.49273908075342], zoom_start=11,
)
rfile = open(
    "./folium_json/jeju-municipalities-geo.json", "r", encoding="utf-8",
).read()
jsonData = json.loads(rfile)
folium.GeoJson(jsonData, name="json_data").add_to(map_osm)
map_osm


# %%
import pandas as pd

filename = "jeju.csv"
df = pd.read_csv(filename, encoding="cp949", header=0)
df = df.drop(columns="Unnamed: 8")
df
# %%
df["인구"] = (
    df["일반현황"]
    .str.split("구")
    .str.get(1)
    .str.split("명")
    .str.get(0)
    .str.split("(")
    .str.get(0)
    .str.split("/")
    .str.get(0)
    .str.strip()
    .astype("int")
)
df["인구"]

# %%
df["지역"] = df["지역"].replace(["제주시", "서귀포시"], ["Jeju", "Seogwipo"])
# %%
df1 = df.groupby(["지역"]).sum()

df1

# %%
map_osm = folium.Map(location=[33.3616649, 126.511657], zoom_start=9,)
rfile = open(
    "./folium_json/jeju-municipalities-geo.json", "r", encoding="utf-8",
).read()
jsonData = json.loads(rfile)
folium.GeoJson(jsonData, name="json_data").add_to(map_osm)
map_osm

#%%

map_osm.choropleth(
    geo_data=jsonData,
    data=df1["인구"],
    columns=[df1.index, df1["인구"]],
    key_on="feature.id",
    fill_color="PuRd",
    legend_name="제주 인구",
)
map_osm


# %%

df2 = df.groupby(["읍면동"]).sum()

df2

# %%
map_osm = folium.Map(location=[33.3616649, 126.511657], zoom_start=9,)
rfile = open("./folium_json/jeju.json", "r", encoding="utf-8",).read()
jsonData = json.loads(rfile)
folium.GeoJson(jsonData, name="json_data").add_to(map_osm)
map_osm


# %%
map_osm.choropleth(
    geo_data=jsonData,
    data=df2["인구"],
    columns=[df2.index, df2["인구"]],
    key_on="feature.id",
    fill_color="YlGnBu",
    legend_name="제주 인구",
)
map_osm


# %%
map_osm.choropleth(
    geo_data=jsonData,
    data=df,
    columns=["읍면동", "인구"],
    key_on="feature.id",
    fill_color="YlGnBu",
    fill_opacity=0.7,
    line_opacity=0.3,
)
map_osm


# %%
