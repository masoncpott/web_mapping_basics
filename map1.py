import folium
import pandas

### create map ###
map1 = folium.Map([45.47001152268444, -122.61397957233314], zoom_start=13, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map", overlay=True, control=True, show=True)

folium.Marker([45.47001152268444, -122.61397957233314], popup="<i>My House New</i>").add_to(fg)



### process the data from the txt file ###
volcano_data = pandas.read_csv("Webmap_datasources/Volcanoes.txt")

latitude = list(volcano_data["LAT"])
longitude = list(volcano_data["LON"])

# len(latitude) == len(longitude) # output = True

### add markers to map that represent each volcano ###
for lat, lon in zip(latitude, longitude):
    folium.Marker(location=[lat, lon]).add_to(fg)

map1.add_child(fg)



map1.save("Map1.html")