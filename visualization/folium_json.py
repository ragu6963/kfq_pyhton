# %%
import folium
import json

map_osm = folium.Map(location=[37.566345, 126.977893])
rfile = open("./folium_json/skorea-provinces-2018-geo.json", "r", encoding="utf-8").read()
jsonData = json.loads(rfile)
folium.GeoJson(jsonData, name="json_data").add_to(map_osm)
map_osm

# %%
map_osm = folium.Map(location=[33.50704277172384, 126.49273908075342], zoom_start=11)
rfile = open("./folium_json/jeju-municipalities-geo.json", "r", encoding="utf-8").read()
jsonData = json.loads(rfile)
folium.GeoJson(jsonData, name="json_data").add_to(map_osm)
map_osm


# %%
