#!/usr/bin/env python3
import cgi, os
import urllib.parse
form = cgi.FieldStorage()
text1 = form.getfirst("newChain", "undef")
print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>
        <p>Successfully</p>
        </body>""")
decodedText = urllib.parse.unquote_plus(text1)
open(os.getcwd() + "/sets/list.txt", "a+").write("\n" + decodedText)
