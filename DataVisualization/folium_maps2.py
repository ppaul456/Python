## Folium Maps
import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library
import folium

print('Folium installed and imported!')

# define the world map
world_map = folium.Map()

# display world map
#world_map.save('world_map.html')

# define the world map centered around Canada with a higher zoom level
world_map = folium.Map(location=[56.130, -106.35], zoom_start=8)

# display world map
#world_map.save('world_map2.html')

##################################################################################
## Stamen Toner Maps
# High-contrast B+W (black and white) maps. 
# They are perfect for data mashups and exploring river meanders and coastal zones.

# create a Stamen Toner map of the world centered around Canada
world_map = folium.Map(location=[56.130, -106.35], zoom_start=4, tiles='Stamen Toner')

# display map
world_map.save('world_StamenToner_map.html')

##Stamen Terrain Maps
# Maps that feature hill shading and natural vegetation colors.
# They showcase advanced labeling and linework generalization of dual-carriageway roads.

# create a Stamen Toner map of the world centered around Canada
world_map = folium.Map(location=[56.130, -106.35], zoom_start=4, tiles='Stamen Terrain')

# display map
world_map.save('world_StamenTerrain_map.html')

## Mapbox Bright Maps
# Maps that quite similar to the default style, except that the borders are not visible with a low zoom level.

# create a world map with a Mapbox Bright style.
world_map = folium.Map(tiles='Mapbox Bright')

# display the map
world_map.save('world_MapboxBright_map.html')

#########################################################################################
##Maps with Markers 

# download and import the data on police department incidents using pandas read_csv() method.
df_incidents = pd.read_csv('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Police_Department_Incidents_-_Previous_Year__2016_.csv')

print('Dataset downloaded and read into a pandas dataframe!')
print(df_incidents.head())

#how many entries there are in dataset
print(df_incidents.shape)

# San Francisco latitude and longitude values
latitude = 37.77
longitude = -122.42
# create map and display it
sanfran_map = folium.Map(location=[latitude, longitude], zoom_start=12)
# display the map of San Francisco
sanfran_map.save('world_sanfran_map.html')

# instantiate a feature group for the incidents in the dataframe
incidents = folium.map.FeatureGroup()

# loop through the 100 crimes and add each to the incidents feature group
for lat, lng, in zip(df_incidents.Y, df_incidents.X):
    incidents.add_child(
        folium.CircleMarker(
            [lat, lng],
            radius=5, # define how big you want the circle markers to be
            color='yellow',
            fill=True,
            fill_color='blue',
            fill_opacity=0.6
        )
    )
# add pop-up text to each marker on the map
latitudes = list(df_incidents.Y)
longitudes = list(df_incidents.X)
labels = list(df_incidents.Category)

for lat, lng, label in zip(latitudes, longitudes, labels):
    folium.Marker([lat, lng], popup=label).add_to(sanfran_map)    
    
# add incidents to map
sanfran_map.add_child(incidents)
sanfran_map.save('world_SanfranCrime_map.html')
# crime category occurred at each marker.