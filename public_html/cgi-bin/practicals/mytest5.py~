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
for row in c:
  # Note the two ways of doing this without a blank "" separator below - either way produces a space around the text string
  # and the <b> bold tags.  Not a major problem as subsequent normal spaces occurring immediately after the first
  # are simply ignored by the web browser however these extra spaces appear in the code
  # We can solve by using a suitable "" separator
  # Or we can build up a string using str() where required as in example5_2.py

  #print("<p>",row[0],"-","<b>",row[1],"</b>","-","{:%d-%m-%y}".format(row[2]),"-","{:%d-%m-%y}".format(row[3]),"</p>")
  print("<p>",row[0],"- <b>",row[1],"</b> -","{:%d-%m-%y}".format(row[2]),"-","{:%d-%m-%y}".format(row[3]),"</p>")
conn.close()


print("</body>")
print("</html>")
