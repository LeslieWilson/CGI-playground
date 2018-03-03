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
		
 <Title>Leslie Cookie Monster's Monster Cookie Demo</Title>

</head>
<body>
 <p>whomever's name appears below, is the Queen of the World.</p>
 <p><b>let it be KNOWN</b></p>""")  

print ("""
<form action= "nateStayawayFromthis.py" method = "get"> Who is the almighty queen?<input name= "question">
	<input value= "submit queen" type="submit">
		</form>

		</body>
		</html> """)


