# Twilio "textme.py" Script

This script is a simple example of sending an SMS text message with a specific message to a single phone number. It requires that you provide account information as well as a phone number to send to in a configuration file outlined below.

## Configuration File

The `textme.py` script looks for a configuration file that it stores in `twilioConfigFile`. Change that path in the script to point to your configuration file with the following format.

The file must contain 4 lines consisting of:

* Twilio Account SID
* Twilio Authentication Token
* Twilio Phone Number
* Recipient Phone Number

An example would look something like:

````
abcdef1234567890abcdef1234567890ab
1234567890abcdef1234567890abcdef
+15554443333
+15555555555
````
