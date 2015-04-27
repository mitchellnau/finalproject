#!/usr/bin/env python
from paypal_functions import *
import cgi
import cgitb; cgitb.enable()
from ConfigParser import SafeConfigParser
import urllib
import socket

parser = SafeConfigParser()
parser.read('paypal_config.ini')

form = cgi.FieldStorage()
#Call to SetExpressCheckout using the shopping parameters collected from the shopping form on index.py and few from config.py
USERACTION_FLAG = parser.get('Credentials','USERACTION_FLAG')
if USERACTION_FLAG == 'True' :
	returnURL = 'http://'+socket.gethostbyname(socket.gethostname())+ '/cgi-bin/PaypalCredit/return.py'
else:
        returnURL = 'http://'+socket.gethostbyname(socket.gethostname())+ '/cgi-bin/PaypalCredit/review.py'
cancelURL = 'http://'+socket.gethostbyname(socket.gethostname())+ '/cgi-bin/PaypalCredit/cancel.py'
# form Fields
form_fields = {}
for key in form.keys():
	form_fields[str(key)] = str(form.getvalue(str(key)))

if form.getvalue("PAYMENTREQUEST_0_ITEMAMT"):
	PAYMENTREQUEST_0_ITEMAMT = form.getvalue("PAYMENTREQUEST_0_ITEMAMT")
	form_fields['L_PAYMENTREQUEST_0_AMT0'] = PAYMENTREQUEST_0_ITEMAMT
	resArray = CallShortcutExpressCheckout (form_fields, returnURL, cancelURL)
   	ack = resArray.get("ACK")[0].upper()
   	if ack=="SUCCESS" or ack=="SUCCESSWITHWARNING":  #if SetExpressCheckout API call is successful
		RedirectToPayPal ( resArray["TOKEN"] )
    
   	else:     	
   		#Display a user friendly Error on the page using any of the following error information returned by PayPal
   		ErrorCode = resArray.get('L_ERRORCODE0')
   		ErrorShortMsg = resArray.get('L_SHORTMESSAGE0')
   		ErrorLongMsg = resArray.get('L_LONGMESSAGE0')
   		ErrorSeverityCode = resArray.get('L_SEVERITYCODE0')
		print "Content-type: text/html\n\n"
   		print "SetExpressCheckout API call failed. "
   		print "Detailed Error Message: " +ErrorLongMsg[0]
   		print "Short Error Message: " +ErrorShortMsg[0]
   		print "Error Code: " +ErrorCode[0]
   		print "Error Severity Code: " + ErrorSeverityCode[0]
	

