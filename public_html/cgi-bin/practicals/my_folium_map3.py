#!/usr/bin/env python3
import cgi
import cgitb
import folium
import sys
import cx_Oracle

with open("/web/s1880452/oracle",'r') as pwf:
    pw = pwf.read().strip()

# try out toner map tiles by adding tiles='Stamen Toner'
map_1 = folium.Map(location=[55.9486,-3.2008],zoom_start=5)

conn = cx_Oracle.connect(dsn="geosgen",user="student",password=pw)
c = conn.cursor()

c.execute("select CASTLE,LAT_Y,LON_X from ancient_castles")

for row in c:
    folium.Marker(row[1:],popup=row[0]).add_to(map_1)

folium.LayerControl().add_to(map_1)

print("Content-type: text/html\n")
print(map_1.get_root().render()) 
