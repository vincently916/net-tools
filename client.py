#!/usr/bin/python

import socket
import sys
import telnetlib
s = socket.socket()

host = "192.168.56.104"
port = 22 


try:
   tn = telnetlib.Telnet(host,port)
   
except socket.error as msg:
   tn = None

if tn is None:
   print "Error connecting to " + str(port) 
   print msg
   sys.exit(1)
else:
  tn.read_until("login:")
tn.close()

#s.connect((host,port))
#print s.recv(1024)
#s.close
