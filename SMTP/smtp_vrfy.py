#!/usr/bin/python
# Simple python script to preform a SMTP vrfy
# with given username and password
##Need to add functionality to read from file

import socket
import sys

if len(sys.argv) != 3:
        print "Usage: vrfy.py <ip address> <username>"
        sys.exit(0)

#Create a Socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Connect to the Server
connect=s.connect((sys.argv[1],25))

#Recieve banner
banner=s.recv(1024)
print banner

#VRFY a user
s.send('VRFY ' + sys.argv[2] + '\r\n')
result=s.recv(1024)
print ("Associated IP: " + sys.argv[1] + "user: " + result)

#Close the socket
s.close(
