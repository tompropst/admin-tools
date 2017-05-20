#! /usr/bin/env python
#****************************************************************************
#* file: textme.py
#* author: Tom Propst
#* Sends the message passed as the sole argument as an SMS message.
#****************************************************************************

#*******************************************************************************
# Copyright 2017 Thomas Propst
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#******************************************************************************/

import sys
import subprocess
import urllib
import urllib2
import xml.etree.ElementTree as ET
import socket

hostName = socket.gethostname()
if len(sys.argv) > 1:
    msgBody = hostName + ": " + sys.argv[1]
else:
    msgBody = hostName + ": <empty message>"

# Twilio stuff
# You must have a file listed below that contains 4 lines for:
# Twilio Account SID
# Twilio Authentication Token
# Twilio Phone Number
# Recipient Phone Number
twilioConfigFile = '../config/twilio.conf'
params = [line.strip() for line in open(twilioConfigFile)]
if len(params) >= 4:
    accountSid = params[0]
    authToken = params[1]
    fromNum = params[2]
    toNum = params[3]

baseUrl = 'https://api.twilio.com/2010-04-01/Accounts/' + \
    accountSid +  '/SMS/Messages'
parameters = {'From' : fromNum,
              'To' : toNum,
              'Body' : msgBody}

data = urllib.urlencode(parameters)
req = urllib2.Request(baseUrl, data)
password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, baseUrl, accountSid, authToken)
handler = urllib2.HTTPBasicAuthHandler(password_mgr)
opener = urllib2.build_opener(handler)

# Install the opener.
# Now all calls to urllib2.urlopen use the opener.
urllib2.install_opener(opener)

response = urllib2.urlopen(req)
result = response.read()

resultElements = ET.ElementTree(ET.fromstring(result))
resultRoot = resultElements.getroot()
for status in resultRoot.iter('Status'):
    print 'Msg Status: ' + status.text

