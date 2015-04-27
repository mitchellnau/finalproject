#!/usr/bin/env python
import cgi,cgitb
import Cookie
import os
import socket
import pickle
from paypal_functions import *
cookie = Cookie.SimpleCookie(os.environ["HTTP_COOKIE"])

#accessing form fields on index page through cookies
_SESSION = pickle.loads(cookie["session"].value)
if not _SESSION:
	_SESSION = {}

# getting access token passed by LoggedIn page and storing in _SESSION variable
form = cgi.FieldStorage()
access_token = form.getvalue('TOKEN')
_SESSION["access_token"] = access_token

#defining return and cancel url for making call to ShortcutExpressCheckout
returnURL = 'http://'+socket.gethostbyname(socket.gethostname()) + '/cgi-bin/SeamlessCheckout/return.py'
cancelURL = 'http://'+socket.gethostbyname(socket.gethostname()) + '/cgi-bin/SeamlessCheckout/cancel.py'

#calling ShortcutExpressCheckout to generate Name value pair String
nvp = CallShortcutExpressCheckout(_SESSION, returnURL,cancelURL)

#if Success use Token generated in name value pair and Redirect To PayPal 
if nvp['ACK'][0] == 'Success':
	_SESSION['token'] = nvp.get('TOKEN')[0]
	RedirectToPayPal(nvp.get('TOKEN')[0])
