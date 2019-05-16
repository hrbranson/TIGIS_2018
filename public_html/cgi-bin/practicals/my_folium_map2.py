#!/usr/bin/env python3
import cgi
import cgitb
import folium
import cx_Oracle

# try out toner map tiles by adding tiles='Stamen Toner'
map_l = folium.Map(location=[55.9486,-3.2008],zoom_start=6)

conn = cx_Oracle.connect("student/train@geosgen")
c = conn.cursor()

c.execute("select castle,LAT_Y,LON_X from ancient_castles")

for row in c:
    folium.Marker(row[1:],popup=row[0]).add_to(map_l)

print("Content-type: text/html\n")
print(map_l.get_root().render()) 
