#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
print("Content-Type: text/html\n")
print("<!DOCTYPE html>")

#The following line will render fine in the web browser
#but will result in much HTML on one line in the html doc produced when
#viewing the page source (which any end user can do!)

print("<head><title>This is the Page Title</title></head>")
print("<body>")
print("<h2>Some content:</h2>")
print("<p>Sample body content.")
print("Further content on a newline in the HTML doc but appears on the same line in the webpage as part of the same paragraph.</p>")

#Blank lines above and below this comment improve python readability only

print("<p>Hello World!</p>")
print("<p>This is my first Python produced HTML page!</p>")

print("</body>")
print("</html>")
