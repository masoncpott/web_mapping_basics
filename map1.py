import folium
import pandas

### create map ###
map1 = folium.Map([45.47001152268444, -122.61397957233314], zoom_start=13, tiles = "Stamen Terrain")

fg = folium.FeatureGroup(name="My Map", overlay=True, control=True, show=True)

folium.Marker([45.47001152268444, -122.61397957233314], popup="<i>My House New</i>").add_to(fg)



### process the data from the txt file ###
volcano_data = pandas.read_csv("Webmap_datasources/Volcanoes.txt")

latitudes = list(volcano_data["LAT"])
longitudes = list(volcano_data["LON"])
elevations = list(volcano_data["ELEV"])
names = list(volcano_data["NAME"])



### add markers to map that represent each volcano ###
def icon_color(elevation):
    if elevation <= 2000:
        return "green"
    if elevation > 2000 and elevation <= 3000:
        return "orange"
    if elevation > 3000:
        return "red"

html = """<h3>%s</h3>
Elevation: %s m """


for lat, lon, el, name in zip(latitudes, longitudes, elevations, names):
    folium.CircleMarker(
        location = [lat, lon], 
        radius = 6, 
        popup = html % (name, str(el)), 
        color = 'grey',
        fill_opacity=0.7, 
        fill=True, 
        fill_color=icon_color(el)
        ).add_to(fg)

fg.add_child(folium.GeoJson(
    data = open("Webmap_datasources/world.json", 'r', encoding="utf-8-sig").read(),
    style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000 
        else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
        else 'red'}
    ))

map1.add_child(fg)

map1.save("Map1.html")