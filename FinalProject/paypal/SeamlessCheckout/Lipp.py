#!/usr/bin/env python
#coding: utf8
import Cookie
import os
import pickle
import datetime
import random
import cgi
import socket
import cgitb; cgitb.enable()
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()

#Taking APPID from config file based on mode is Live or Sandbox
parser.read('paypal_config.ini')
if parser.get('Credentials','SANDBOX_FLAG') == 'True':
	app_id = parser.get('Credentials','PP_CLIENT_ID_SANDBOX')
	auth_end_value = "\"authend\":'sandbox',"
else:
	app_id = parser.get('Credentials','PP_CLIENT_ID')
	auth_end_value = ""

#return url where LIPP will redirect to
#For test purposes use the following:
#returnURL = 'http://localhost/cgi-bin/SeamlessCheckout/Loggedin.py'
returnURL = 'http://'+socket.gethostbyname(socket.gethostname()) + '/cgi-bin/SeamlessCheckout/Loggedin.py'

#putting form fields value on index page in _SESSION variable
_SESSION={}
form = cgi.FieldStorage()
_SESSION["Payment_Amount"] = form.getvalue("PAYMENTREQUEST_0_AMT")
_SESSION['currencyCodeType'] = form.getvalue('currencyCodeType')
_SESSION['paymentType'] = form.getvalue('paymentType')
_SESSION['L_PAYMENTREQUEST_0_NAME0'] = form.getvalue('L_PAYMENTREQUEST_0_NAME0')
_SESSION['L_PAYMENTREQUEST_0_NUMBER0'] = form.getvalue('L_PAYMENTREQUEST_0_NUMBER0')
_SESSION['L_PAYMENTREQUEST_0_DESC0'] = form.getvalue('L_PAYMENTREQUEST_0_DESC0')
_SESSION['L_PAYMENTREQUEST_0_QTY0'] = form.getvalue('L_PAYMENTREQUEST_0_QTY0')
_SESSION['PAYMENTREQUEST_0_ITEMAMT'] = form.getvalue('PAYMENTREQUEST_0_ITEMAMT')
_SESSION['PAYMENTREQUEST_0_TAXAMT'] = form.getvalue('PAYMENTREQUEST_0_TAXAMT')
_SESSION['PAYMENTREQUEST_0_SHIPPINGAMT'] = form.getvalue('PAYMENTREQUEST_0_SHIPPINGAMT')
_SESSION['PAYMENTREQUEST_0_HANDLINGAMT'] = form.getvalue('PAYMENTREQUEST_0_HANDLINGAMT')
_SESSION['PAYMENTREQUEST_0_SHIPDISCAMT'] = form.getvalue('PAYMENTREQUEST_0_SHIPDISCAMT')
_SESSION['PAYMENTREQUEST_0_INSURANCEAMT'] = form.getvalue('PAYMENTREQUEST_0_INSURANCEAMT')
_SESSION['PAYMENTREQUEST_0_AMT'] = form.getvalue('PAYMENTREQUEST_0_AMT')
_SESSION['LOGOIMG'] = form.getvalue('LOGOIMG')
_SESSION['L_PAYMENTREQUEST_0_AMT0'] = form.getvalue('PAYMENTREQUEST_0_ITEMAMT')

#storing _SESSION variable to be used later in Cookies
expiration = datetime.datetime.now() + datetime.timedelta(days=30)
cookie = Cookie.SimpleCookie()
cookie["session"]=pickle.dumps(_SESSION)
cookie["session"]["expires"] = expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST")
print cookie.output()

#Form and LIPP button to be displayed on the page	
import header
htmlcode = """\

<span class="span4">
  </span>
  <span class="span5">
<table>
   <tr>
      <td>
         <form method="POST">
            <legend>Log in with MERCHANT</legend>
            <p><label for="email">Email:</label>
               <input type="text" name="email" id="email" required>
            </p>
            <p><label for="password">Password:</label>
               <input type="password" name="password" id="password" required>
            </p>
            <p><button type="submit" class="btn btn-primary btn-medium">Log In</button></p>
         </form>
         <p class="tiny"><a href="#">Create an account</a></p>
      </td>
      <td>
         <div class="or">or</div>
      </td>
      <td>
      
         <span id="myContainer" data-paypal-button="true"></span>
         <!-- Scripts for getting the Login with PayPal button-->
         <script src="https://www.paypalobjects.com/js/external/api.js"></script>
        <script> 
            paypal.use( ["login"], function(login) {
				login.render ({
                "appid":'%s',%s
                "scopes": "openid profile email address phone https://uri.paypal.com/services/paypalattributes https://uri.paypal.com/services/expresscheckout",
                "containerid": "myContainer",
                "locale": "en-us",
                "returnurl": '%s'
              });
            });
         </script>
      </td>
   </tr>
</table>
</span>
<span class="span3">
</span>""" % (app_id, auth_end_value, returnURL)

print htmlcode

import footer
