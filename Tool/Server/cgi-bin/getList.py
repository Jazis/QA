#!/usr/bin/env python3
import cgi
import html
import os

form = cgi.FieldStorage()
username = form.getfirst("username", "")
usernameValue = html.escape(username)

print("Content-type: text/html")
print("Status: 200")

# print ("""Status:503\n
# Content-type: text/html\n""")

pathWithFiles = os.getcwd() + "/files/" + usernameValue + "/"

result = []

result.append("<!DOCTYPE HTML>")
result.append("<html>")
result.append("<meta charset=\"utf-8\">")
result.append("<title>Result</title>")
result.append("</head>")
result.append("<body>")
for file in os.listdir(pathWithFiles):
    result.append("<p>\"" + file + "\"</p>")
result.append("</body></html>")

for elem in result:
    print(elem)