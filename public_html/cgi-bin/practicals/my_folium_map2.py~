#!/usr/bin/env python3
import cgitb
import cgi
import folium

# some interesting locations
drummondSt = [55.948162, -3.184111]
kb = [55.923998, -3.174950]

# try out toner map tiles by adding tiles='Stamen Toner'
map_l = folium.Map(location=drummondSt,zoom_start=14)

folium.Marker(drummondSt,popup="This is Drummond St!").add_to(map_l)
folium.Marker(kb,popup="<b>This is KB!</b>").add_to(map_l)

print("Content-type: text/html\n")
print(map_l.get_root().render())
