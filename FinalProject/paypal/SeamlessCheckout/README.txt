SEAMLESS CHECKOUT WITH PAYPAL DEMO 

1) Install Apache2 in your system.

2) Copy SeamlessCheckout-Python folder to apache cgi-bin directory as SeamlessCheckout.

3) Copy img,js, CSS and README.txt file in /var/www/(for Linux) inside xampp/htdocs for windows.

4) Log on to https://developer.paypal.com with your PayPal credentials. 

5) To integrate Login with PayPal to your website, either use the credentials provided on paypal_config.ini OR
create a new REST app at https://developer.paypal.com/webapps/developer/applications/createapp with following steps:
    (1) Give a suitable name to the app and click "Create App". It will show you a page with App Details, some of them already filled.
    (2) Click on "Edit" next to the App redirect URLs.
    (3) In the App return URL (test) field enter: "http://my_domain/python_code_folder_name/Loggedin.py"
        Here, my_domain will be your machine IP Address or localhost if hosting on your own machine.  
        The python_code_folder_name is the name of the folder under which the downloaded code resides.
    (4) In the REST API credentials section, note down the Client ID and Secret. It will be used in step 7-(3).
    (5) In the App Capabilities section, click on Advanced Options next to Login with PayPal.
    (6) Under Information requested from customers, you will see what are called "scopes". The scope attributes represent the data that you are requesting the customers to share. 
        Check all of them (Personal Information, Address Information and Account Information). 
        If you click on customize next to any one, say Personal information, you will see individual attributes listed and checked there.
        *Remember, the scopes checked here have to match the ones listed in Lipp.py More on this in step 7-(4).
        [Later - If you want to customize you can check/uncheck the individual attributes and make sure they match the scopes in paypal_config.ini]
        If you want to know more about scopes read here: https://developer.paypal.com/docs/integration/direct/identity/attributes/
    (7) In the Privacy Policy URL textbox, enter your url: http://my_domain/python_code_folder_name/privacyPolicy.py
        Similarly, for the User Agreement URL field, enter your url: http://my_domain/python_code_folder_name/userAgreement.py
        Even here, my_domain and python_code_folder_name are same as explained in step 5-(3).
    (9) Click on "Preview the customer consent page" and see how it will appear to the users.
    (10) Under the Additional PayPal permissions, check the Seamless Checkout and Allow the customers who haven't yet confirmed their email address with PayPal, to log in to your app. 
         Here, remember that the scope "https://uri.paypal.com/services/expresscheckout" listed in SCOPES in paypal_config.ini is for Seamless checkout.  
    (11) Click Save to save all these settings for your app.

6) If you plan to use the credentials provided, you do not need to create seller account. If not, you can create a Seller account (a Business account) and buyer accounts at https://developer.paypal.com/webapps/developer/applications/accounts/create (This was tested using OSX's Apache Webserver in: /Library/WebServer/CGI-Executables, and the /Library/WebServer/CGI-Executables/SeamlessCheckout/Loggedin.py was set to http://localhost/cgi-bin/SeamlessCheckout/Loggedin.py)

7) If you plan to use the REST app and seller credentials provided, you do not need to do this step. If you are using your own REST app and seller, update the following fields in the specified files:
    (1) In paypal_config.ini, update the values of the form fields: PP_USER_SANDBOX, PP_PASSWORD_SANDBOX and PP_SIGNATURE_SANDBOX  - your seller credentials. Use the Seller whose test account email appear in the Rest API credentials in the REST app.
    (2) For getting the credentials of the seller go to the profile of the seller in the Sandbox accounts.
    (3) In paypal_config.ini update the values of the form fields PP_CLIENT_ID_SANDBOX, PP_CLIENT_SECRET_SANDBOX- Use these from step 5-(4) 
    (4) In Lipp.py, "scopes" in Login with Paypal button script - All scopes have been listed in SCOPES, you may remove the ones which you do not need. But make sure the scopes in the REST app on https://developer.paypal.com match ones which you keep here.
    (5) In Lipp.py, "returnurl" - This is the URL where Login with Paypal will return to. If you have followed step 5-(3) no change is needed. If not make sure, the url in step 5-(3) in the REST app matches returnurl in Lipp.py.
    (6) In Lipp.py, "authend" is "sandbox" for testing. But, when live, the Login Button script on Lipp.py will not have the authend field. Refer https://developer.paypal.com/webapps/developer/docs/integration/direct/identity/button-js-builder/
    (7) SANDBOX_FLAG in paypal_config.ini will be True for working with sandbox and False for live.
    (8) Lipp.py: update the values for returnURL to match your site as well as the returnURL set in 5->(3) above

8) Start the server.

9) Open the website in the browser and access as http://my_domain/python_code_folder_name/index.py

10) If you get any Firewall warning, add rule to the Firewall to allow incoming connections for your application.

11) Click on "PROCEED TO CHECKOUT" , then start the Login with Paypal flow using the buyer sandbox account previously created and checkout. You're done!

12) You will find further instructions for integrating Seamless Checkout on your website on the home page of the demo website.

