# %%
import folium


# %%
map_osm = folium.Map(location=[35.8365771, 128.5065935], zoom_start=15)
# map_osm.save("map.html")
map_osm


# %%
map_osm = folium.Map(location=[35.8365771, 128.5065935], zoom_start=15, tiles="Stamen Terrain")
# map_osm.save("map.html")
map_osm


# %%
map_osm = folium.Map(location=[35.8365771, 128.5065935], zoom_start=15)
folium.Marker([35.8365771, 128.5065935], popup="KFQ").add_to(map_osm)
map_osm


# %%
map_osm = folium.Map(location=[35.8365771, 128.5065935], zoom_start=15)
folium.Marker(
    [35.8365771, 128.5065935], popup="KFQ", icon=folium.Icon(color="red", icon="info-sign")
).add_to(map_osm)
folium.CircleMarker([35.8365771, 128.5065935], radius=50, color="white", fill_color="blue").add_to(
    map_osm
)
map_osm


# %%
