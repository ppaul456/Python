#Install folium package
import folium
from IPython.display import display

canada_location = [56.130, -106.35]
#define the map
canada_map = folium.Map(location=canada_location, zoom_start=4)

canada_map.save('canada_map.html')
#call save function

##add red marker to Ontario(安大略省)

# create a feature group
ontario = folium.map.FeatureGroup()

# style the feature group
ontario.add_child(
    folium.CircleMarker(
        [51.25,-85.32], radius = 5, color = "red", fill_color = "Red"
    )
)

## add the feature group to the map
canada_map.add_child(ontario)

# lable the marker
folium.Marker([51.25,-85.32], popup="ontario").add_to(canada_map) 

canada_map.save('canada_map2.html')

Spain_map = folium.Map(location=[-40.4637, -3.7492], zoom_start=6, tiles='Stamen Terrain')
Spain_map.save('Spain_map.html')