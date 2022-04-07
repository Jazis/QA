#!/usr/bin/env python3
import cgi, os
import cgitb; cgitb.enable()
form = cgi.FieldStorage()
# Get filename here.
# scriptPath = os.getcwd().replace(os.getcwd().split("/")[-1], "")
scriptPath = os.getcwd() + "/"
fileitem = form['filename']
username = form['username']
fullpath = scriptPath + "files/" + username.value + "/"
try:
    os.system("mkdir " + fullpath)
except:
    pass
# Test if the file was uploaded
if fileitem.filename:
   # strip leading path from file name to avoid
   # directory traversal attacks
   fn = os.path.basename(fileitem.filename)
   open(scriptPath + "files/" + username.value + "/" + fn, 'wb').write(fileitem.file.read())
   message = 'The file "' + fn + '" was uploaded successfully'
 
else:
   message = 'No file was uploaded'
 
print("""\
Content-Type: text/html\n
<html>
<body>
   <p>%s</p>
</body>
</html>
""" % (message,))
