#!/usr/bin/env python3
import cgitb
import cx_Oracle
import folium
cgitb.enable(format='text')
from jinja2 import Environment, FileSystemLoader

#render the template
def print_html():
    env = Environment(loader=FileSystemLoader('.'))
    temp = env.get_template('castles.html')
    inpName ='Hattie'
    inpCastles = castleHtml()
    inpFol = foliumMap()
    print(temp.render(name = inpName, castles = inpCastles, map=inpFol))

def castleHtml():
    conn = cx_Oracle.connect("student/train@geosgen")
    c = conn.cursor()
    c.execute("SELECT * FROM ancient_castles")
    html = ''
    for row in c:
        html = html + row[0] + " - " + row[1] + " -" + row[4] + "<br>"
    conn.close()
    return html

def foliumMap():
    map_1 = folium.Map(location=[55.9486,-3.2008],zoom_start=6)
    conn = cx_Oracle.connect("student/train@geosgen")
    c = conn.cursor()
    c.execute("select castle,LAT_Y,LON_X from ancient_castles")
    for row in c:
        folium.Marker(row[1:],popup=row[0]).add_to(map_1)
    conn.close()
    return map_1.get_root().render()

if __name__ == '__main__':
    print_html()
