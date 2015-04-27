#!/usr/bin/env python
#coding: utf8
import header, socket
logoUrl = 'http://'+socket.gethostbyname(socket.gethostname()) + '/img/logo.jpg'
print """\
<div class="row-fluid">
	<div class="span5">
		<div class="row-fluid">
			<div class="span6 inner-span">

				<!--Form containing item parameters and seller credentials needed for SetExpressCheckout Call-->
				<form action="Lipp.py" method="POST">
					<td>
						<h3>DIGITAL SLR CAMERA</h3> <img src="../../img/camera.jpg" width="300"
						height="250" /> <!--Demo Product details -->
						<table>
							<tr>
								<p class="lead">Buyer Credentials:</p>
							</tr>
							<tr>
								<td>Email-id:</td>
								<td><input type="text" id="buyer_email" name="buyer_email"
									readonly></input></td>
							</tr>
							<tr>
								<td>Password:</td>
								<td><input type="text" id="buyer_password"
									name="buyer_password" readonly></input></td>
							</tr>
						</table>
			</div>
			<div class="span6 inner-span">
				<p class="lead">Item Specifications:</p>
				<table>
					<tr>
						<td>Item Name:</td>
						<td><input type="text" name="L_PAYMENTREQUEST_0_NAME0"
							value="DSLR Camera"></input></td>
					</tr>
					<tr>
						<td>Item ID:</td>
						<td><input type="text" name="L_PAYMENTREQUEST_0_NUMBER0"
							value="A0123"></input></td>
					</tr>
					<tr>
						<td>Description:</td>
						<td><input type="text" name="L_PAYMENTREQUEST_0_DESC0"
							value="Autofocus Camera"></input></td>
					</tr>
					<tr>
						<td>Quantity:</td>
						<td><input type="text" name="L_PAYMENTREQUEST_0_QTY0"
							value="1" readonly></input></td>
					</tr>
					<tr>
						<td>Price:</td>
						<td><input type="text" name="PAYMENTREQUEST_0_ITEMAMT"
							value="10.00" readonly></input></td>
					</tr>
					<tr>
						<td>Tax:</td>
						<td><input type="text" name="PAYMENTREQUEST_0_TAXAMT"
							value="2" readonly></input></td>
					</tr>
					<tr>
						<td>Shipping Amount:</td>
						<td><input type="text" name="PAYMENTREQUEST_0_SHIPPINGAMT"
							value="5" readonly></input></td>
					</tr>
					<tr>
						<td>Handling Amount:</td>
						<td><input type="text" name="PAYMENTREQUEST_0_HANDLINGAMT"
							value="1" readonly></input></td>
					</tr>
					<tr>
						<td>Shipping Discount:</td>
						<td><input type="text" name="PAYMENTREQUEST_0_SHIPDISCAMT"
							value="-3" readonly></input></td>
					</tr>
					<tr>
						<td>Insurance Amount:</td>
						<td><input type="text" name="PAYMENTREQUEST_0_INSURANCEAMT"
							value="2" readonly></input></td>
					</tr>
					<tr>
						<td>Total Amount:</td>
						<td><input type="text" name="PAYMENTREQUEST_0_AMT" value="17"
							readonly></input></td>
					</tr>
					
					<tr>
						<td><input type="hidden" name="LOGOIMG"
							value=""" + logoUrl + """></input></td>
					</tr>
					<tr>
						<td>Currency Code:</td>
						<td><select id="currencyCodeType" name="currencyCodeType">
								<option selected value="USD">USD</option>
								<option value="BRL">BRL</option>
								<option value="CAD">CAD</option>
								<option value="CZK">CZK</option>
								<option value="DKK">DKK</option>
								<option value="EUR">EUR</option>
								<option value="HKD">HKD</option>
								<option value="HUF">HUF</option>
								<option value="ILS">ILS</option>
								<option value="JPY">JPY</option>
								<option value="NOK">NOK</option>
								<option value="MXN">MXN</option>
								<option value="NZD">NZD</option>
								<option value="PHP">PHP</option>
								<option value="PLN">PLN</option>
								<option value="GBP">GBP</option>
								<option value="SGD">SGD</option>
								<option value="SEK">SEK</option>
								<option value="CHF">CHF</option>
								<option value="TWD">TWD</option>
								<option value="THB">THB</option>
								<option value="TRY">TRY</option>
						</select> <br></td>
					</tr>
					<tr>
						<td>Payment Type:</td>
						<td><select name="paymentType">
								<option value="Sale">Sale</option>
						</select><br></td>
					</tr>
					<tr>
						<td><input type="submit" class="btn btn-primary btn-large"
							value="PROCEED TO CHECKOUT"></input></td>
					</tr>
				</table>
			</div>
		</div>


		</form>
	</div>
	<div class="span2"></div>
	<div class="span5">




		<p class="lead">README:</p>

		1) You will need Seller account, buyer account and REST app to test
		the Login with PayPal flow. <br> a. Use the default seller and
		buyer account credentials provided on the page OR create your own
		Seller account (a Business account) and buyer accounts at <a
			href="https://developer.paypal.com/webapps/developer/applications/accounts/create"
			target=_blank>developer.paypal.com</a> <br>b. Use pre created
		REST app credentials provided on the page OR create your own REST app
		at <a
			href="https://developer.paypal.com/webapps/developer/applications/createapp"
			target=_blank>developer.paypal.com create app</a>. For detail
		instructions check <a href="../../README.txt" target=_blank>readme.txt</a> <br>c.
		If you create your own seller and REST app, enter the seller and REST
		app credentials in the config.ini file <br>
		<br> 2) Make following changes in config.properties: -
		SANDBOX_FLAG: Kept true for working with Sandbox, it will be false for
		live. <br> 3) If you get any Firewall warning, add rule to the
		Firewall to allow incoming connections for your application. <br>
		4) Click on Proceed to Checkout, then use Login with PayPal using a
		buyer sandbox account. And continue your seamless checkout. You're
		done! <br> 5) For trying out Mobile-EC, change the user-agent of
		your browser by installing a user agent switcher plugin and see how
		your website will appear on mobile devices.
		</p>
		<br>
		<br>
		<!-- Button to trigger modal -->
		<a href="#myInstructionModal" role="button" class="btn btn-primary"
			data-toggle="modal">Instructions to integrate Seamless Checkout
			on your Website</a>

		<!-- Modal -->
		<div id="myInstructionModal" class="modal hide fade" tabindex="-1"
			role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
			<div class="modal-header">
				<button type="button" class="close" data-dismiss="modal"
					aria-hidden="true">×</button>
				<h3 id="myModalLabel">Instructions to integrate Seamless
					Checkout on your Website</h3>
			</div>
			<div class="modal-body">
				<p class="lead">Instructions to integrate on your website</p>
				1) Copy the files and folders under 'SeamlessCheckout' package to
				the same location where you have your shopping cart page. <br>

				2) Create a new REST app at <a
					href="https://developer.paypal.com/webapps/developer/applications/createapp">here</a>
				with the steps provided in <a href="../../README.txt" target="_blank">readme.txt
					point #4</a> Note: Do not use the default REST credentials provided on
				this page for your testing. <br> 3) Copy the following
				&lt;form&gt; .. &lt;/form&gt; to your shopping cart page. Change the
				action attribute of this form to point to your login page. Enter the
				values for the SELLER_USERNAME, SELLER_PASSWORD, SELLER_SIGNATURE,
				SELLER_REST_APP_CLIENT_ID and SELLER_REST_APP_CLIENT_SECRET text
				fields using your credentials. <br>
				<br> <font size=2 color="#000080"> &lt;form action="PATH
					TO YOUR LOGIN PAGE HERE" method="POST"&gt;&lt;/input&gt;<br>

					&lt;input type="hidden" name="PAYMENTREQUEST_0_AMT"
					value="10.00"&gt;&lt;/input&gt;<br> &lt;input type="hidden"
					name="currencyCodeType" value="USD"&gt;&lt;/input&gt;<br>
					&lt;input type="hidden" name="paymentType"
					value="Sale"&gt;&lt;/input&gt;<br> <i> &lt;!--Pass
						additional input parameters based on your shopping cart. For
						complete list of all the parameters <a
						href="https://developer.paypal.com/webapps/developer/docs/classic/api/merchant/SetExpressCheckout_API_Operation_NVP/"
						target=_blank>click here</a>
				</i> --&gt;<br> &lt;input type="submit" class="btn btn-primary
					btn-large" value="Proceed to Checkout"&gt;&lt;/input&gt;<br>
					&lt;/form&gt;<br>
				</font> <br> 4) Open "YOUR LOGIN PAGE". From Lipp.java copy the below
				to YOUR LOGIN PAGE:<br> &nbsp;&nbsp;a. Cookie parameters that
				stores the parameters needed for SetExpressCheckout call. <br>

	<textarea style="height: 150px; width: 700px";> 
/* Store the parameters needed for SetExpressCheckout call and the LIPP REST app credential */s
                                 
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

expiration = datetime.datetime.now() + datetime.timedelta(days=30)
cookie = Cookie.SimpleCookie()
cookie["session"]=pickle.dumps(_SESSION)
cookie["session"]["expires"] = expiration.strftime("%a, %d-%b-%Y %H:%M:%S PST")
print cookie.output()
                                   
       </textarea>
				<br> &nbsp;&nbsp;b. Login with PayPal button by copying the
				code given in Lipp.py between:<br> <font size=2
					color="#000080"> &lt;span id="myContainer"
					data-paypal-button="true">&lt;/span&gt;<br> <!-- Scripts for getting the Login with PayPal button-->
					&lt;script
					src="https://www.paypalobjects.com/js/external/api.js"&gt;
					&lt;/script&gt;<br> &lt;script&gt;<br> <label>paypal.use( ["login"], function(login) {
						login.render ({ "appid":"YOUR CLIEND ID",<br>
						"authend":"sandbox", <!-- For live remove authend paramter --> <br>
						"scopes": "openid profile email address phone
						https://uri.paypal.com/services/paypalattributes
						https://uri.paypal.com/services/expresscheckout",<br>
						"containerid": "myContainer",<br> "locale": "en-us",<br>
						"returnurl": "YOUR RETURN PAGE URL"<br> });<br> });
				</label><br> &lt;/script&gt;<br>

				</font> <br> 5) In the return_url attribute above, replace
				YOUR_RETURN_PAGE with YOUR RETURN PAGE name. <br> 6)Open your
				browser and go to your page where you have the Proceed to checkout
				button. Click on Proceed to Checkout, then use Login with Paypal
				with a buyer sandbox account and complete the checkout flow.

			</div>
			<div class="modal-footer">
				<button class="btn" data-dismiss="modal" aria-hidden="true">Close</button>
			</div>
		</div>
	</div>



	<!--Script to dynamically choose a seller and buyer account to render on index page-->
	<script type="text/javascript">
		function getRandomNumberInRange(min, max) {
			return Math.floor(Math.random() * (max - min) + min);
		}

		var buyerCredentials = [ {
			"email" : "ron@hogwarts.com",
			"password" : "qwer1234"
		}, {
			"email" : "sallyjones1234@gmail.com",
			"password" : "p@ssword1234"
		}, {
			"email" : "joe@boe.com",
			"password" : "123456789"
		}, {
			"email" : "hermione@hogwarts.com",
			"password" : "123456789"
		}, {
			"email" : "lunalovegood@hogwarts.com",
			"password" : "123456789"
		}, {
			"email" : "ginnyweasley@hogwarts.com",
			"password" : "123456789"
		}, {
			"email" : "bellaswan@awesome.com",
			"password" : "qwer1234"
		}, {
			"email" : "edwardcullen@gmail.com",
			"password" : "qwer1234"
		} ];

		var randomBuyer = getRandomNumberInRange(0, buyerCredentials.length);

		document.getElementById("buyer_email").value = buyerCredentials[randomBuyer].email;
		document.getElementById("buyer_password").value = buyerCredentials[randomBuyer].password;
	</script>
</div>""" 
import footer
