#!/usr/bin/env python3
def get_environment():
	import os
	return os.environ

def get_name():
	import re
	env = get_environment()
	from_form = re.search(r'formname=(\w+)', env.get('QUERY_STRING', ''))
	from_cookie = re.search(r'cookiename=(\w+)', env.get('HTTP_COOKIE', ''))
	name = ''
	if from_form:
		name = from_form.groups()[0]
	elif from_cookie:
		name = from_cookie.groups()[0]
	if name:
		return name
	else:
		return 'BOJANGLES'

queens_name = get_name()
print ("Set-Cookie: cookiename={}".format(queens_name))
print ("Content-Type: text/html")
print ("\n")
	


print ("""
<!doctype html>
<html>
<head>
<title>Leslie Cookie Monster's Monstah Cookie Demo</title>
<link rel= "stylesheet"
		href="https://fonts.googleapis.com/css?family=Averia+Serif+Libre">
<link rel="stylesheet"
	href="https://fonts.googleapis.com/css?family=Anonymous+Pro">
<style type="text/css">
		
body { font-family: 'Averia Serif Libre', serif; }
td { border: 1px solid; }
table {
margin: 1em;
font-family: 'Anonymous Pro', monospace;
font-size: 60%;
}
caption {
text-align: left;
margin-left: 2em;
font-weight:bold;
}
h1, footer { color:#666; }
footer {
font-size: 80%;
}
</style>
</head>
<body>
 <p>whomever's name appears below, is the Queen of the World.</p>
""")

print ("""
 <p><b>let it be KNOWN
<span style="font-weight:bold; color:{0};">{0}</span>.</b></p>
""").format(queens_name)

print ("""
<form action= "CookieDemo.py" method = "get"> Who is the almighty queen?<input name= "question">
	<input value= "submit queen"style= "font-size:0.6em;  type="submit">
</form>
""")

print("<table><caption>environment</caption>"
env = get_environment())
for key in sorted(env.keys()):
	print("<tr><td>{}</td><td>{}</td></tr>").format(key, env,[key]))
print( "</table>")

print( """
<footer style="float:right">
Leslie Wilson | MIT License | 2018 | leslie@leslienate.tech |

</footer>
</body>
</html> 
""")
 

