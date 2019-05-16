#!/usr/bin/env python3

import cgi
import json
from jinja2 import Environment, FileSystemLoader

# import main code class
import fieldsFindsLibrary as ff

# get any submitted form values for filtering use
params = cgi.FieldStorage()

# build modal html
try:
    site = ff.FindModal(params)
    content = site.render()

    env = Environment(loader=FileSystemLoader('.'))
    modal = env.get_template('templates/modal.html')
    print(modal.render(ModalContent=json.dumps(content)))
    # use json.dumps to convert python object to js string

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
