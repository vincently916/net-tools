#!/usr/bin/env python

import socket,sys

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = sys.argv[1]
port = int(sys.argv[2])


result = s.connect_ex((host,port))

if result == 0:
  print 'port ' + str(port) + ' is open'
else:
  print 'port ' + str(port) + ' is closed' 
