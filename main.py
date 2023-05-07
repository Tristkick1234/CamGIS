import pandas as pd
import folium
import math

df = pd.read_csv("cm.csv")
df.head()
#reads the data from the file





loc_center = [df['lat'].mean(), df['lng'].mean()]
#determines the city

map1 = folium.Map(location = loc_center, tiles='Openstreetmap', zoom_start = 5, control_scale=True)
#sets the map and little nuances like zoom and controlability

for index, loc in df.iterrows():
    #for every location
    
    pop_color = "black"
    if loc['population'] > 1000000:
        pop_color= 'pink'
    else:
        pop_color="red"

    folium.CircleMarker([loc['lat'], loc['lng']],     radius=math.sqrt(loc['population']/1000/3.14) ,fill_color=pop_color, weight=1, popup=loc['population']).add_to(map1) 
    folium.LayerControl().add_to(map1)

    #make a circle that centers on the point, sizes and put on map

map1





