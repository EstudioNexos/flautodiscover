{% filter markdown %}
Setup your email account in Mail (Mac Mail)
=============

This guide will show step-by-step instructions for setting up email account in Mail on MacOS.

* Add a New Account
* Incoming Mail Server Settings
* Outgoing Mail Server Settings
* Complete Set Up on Yosemite OS

Add a New Account
-----------------
![alt text](/static/doc/gmaildroid-es-ES-1.png **Logo Title Text 1**)

* Choose Preferences, from the Mail menu.
* The Mail Menu
* Select Preferences.
* Click on the Accounts tab.
* On the Accounts window, click the + (plus) sign.
* Create a new Account

Account Settings
-----------------

* Choose Add Other Mail Account
* Account types in Mac Mail
* Enter your Full Name, or as you would like it to appear on your sent email.
* New Account Creation Window
* Replace example.com with your own domain name.
* Enter your Email Address:.
* Enter your email account's Password.
* Click the Continue button.
* A message should appear saying **Account must be manually configured**. Click Next.

Incoming Mail Server Settings
-----------------------------

When entering the information for your Incoming Mail Server you will need to decide if you would like to use POP3 or IMAP. POP3 will download and remove all of the emails from our server, whereas IMAP will synchronize the emails between your email client(s) and our server. IMAP is recommended if you will be using this email account with multiple devices since they will all synchronize.
Mail - Account Type
Replace example.com with your own domain name.

* Choose your account type. You may select either POP or IMAP.

* Click here for an explanation on the differences between POP3 and IMAP
* Please enter mail.example.com as the Incoming mail server, replacing example.com with your own domain name.
* Enter your full email address as the User Name.
* Enter the Password of your email account.
* Click Next.

Incoming Mail Server Info
-------------------------

* For Path Prefix, please enter INBOX.
* If you are using IMAP, make sure you are using either port 143 with no SSL -OR- port 993 with SSL.
* If you are using POP3, make sure you are using either port 110 with no SSL -OR- port 995 with SSL.
* Authentication should be set to Password.

SSL Certificate Warning
-----------------------

If you choose to use SSL, you may receive a message warning you that the certificate is not trusted. If you receive this message, follow these steps:

* Click Show Certificate.
* The show image button.
* Check the box to always trust the certificate.
* The always trust option.
* Click Connect.

Outgoing Mail Server Settings
-----------------------------

Outgoing Mail Server Window
Replace example.com with your own domain name.

* The Outgoing Mail Server is the same as your incoming mail server. Again, this will be something like mail.example.com
* Enter your full email address as the User Name.

* Note: Outgoing username and password could say **optional** in the field. Please be sure to add your username and password to it.
* Enter the Password of your email account.
* You may receive a message saying Additional account information required.
* For the port number, you can use port 26 with no SSL or port 465 with SSL.
* Make sure the Authentication is set to Password.
* Click the Create button.

Complete Set Up on Yosemite OS
------------------------------ 

If you are running Yosemite you may want to change two options to make sure that your account settings don't change. These steps only apply to apple computers running Yosemite.

* Choose Preferences, from the Mail menu.
* The Mail Menu
* Select Preferences.
* Click on the Accounts tab.
* Click on Advanced.
* Uncheck the option labeled **Automatically detect and maintain settings**.
* Advanced settings screen in mac mail.
* Now Click on Account Information
* Under Outgoing Mail Server(SMTP) select the **Edit SMTP Server List** option.
* Click Advanced.
* Uncheck the option labeled **Automatically detect and maintain settings**.
* Advanced outgoing settings screen in mac mail.
* Click OK
{% endfilter %}
