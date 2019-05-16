#!/usr/bin/env python3

"""
Main entry point for the web application
"""

import cgi

# import main code class
import fieldsFindsLibrary as ff

# get any submitted form values for filtering use
params = cgi.FieldStorage()

try:
    site = ff.FieldsFinds(params)
    content = site.render()
    print(content)

except Exception as e:
    print("Content-Type: text/html\n")
    print("<!DOCTYPE html>")
    print("<head><title>Error</title></head>")
    print("<body>")
    print("<pre>")
    print("Something has gone wrong!")
    print(e)
    print("</pre>")
    print("</body></html>")
