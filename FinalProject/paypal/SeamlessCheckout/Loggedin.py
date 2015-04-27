#!/usr/bin/env python
import cgi,cgitb
from paypal_functions import *
import urllib2
import json

#capturing access token generated by PayPal
form = cgi.FieldStorage()
code = form.getvalue('code')

#if successfully captured close LIPP window and process next steps in parent window by sending access token value	
if code is not None:
	access_token = acquire_access_token(code)
	if access_token is not None:
		
		print "Content-Type: text/html;charset=utf-8\n\n"
		print "<!DOCTYPE html>"
		html = """\
	
		<script type="text/javascript">
		window.opener.location.href ="expresscheckout.py?TOKEN={access_token}";
		window.close();
		</script>
		"""
		print html.format(access_token=access_token)
	else:
		raise Exception("Error Fetching Access Token")
		

	
	
      
