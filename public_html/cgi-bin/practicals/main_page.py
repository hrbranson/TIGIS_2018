#!/usr/bin/env python3

f = open('main_page.html','w')

message = """<html>
<head></head>
<body><p>Archaeological finds in agricultural fields</p><body>
</html>"""

f.write(message)
f.close()

