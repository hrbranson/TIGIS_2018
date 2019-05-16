#!/usr/bin/env python3
import cx_Oracle
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")
print("<!DOCTYPE html>")
# An alternative way of shortening code listing length while
# keeping HTML readable
print("<head>\n<title>The Crop Report</title>\n</head>\n")

print("<body>")

conn = cx_Oracle.connect("student/train@geosgen")
c = conn.cursor()
c.execute("SELECT * FROM GISTEACH.CROPS")

#print("<table>")
#print('<table style="width:100%;border:1px solid black">')
print("<table style=\"width:100%;border:1px solid black\">")
for row in c:
     # print(row[0],"-",row[1])
     print("<tr><td>",row[0],"</td><td>",row[1],"</td></tr>")
conn.close()
print("</table>")


print("</body>")
print("</html>")

