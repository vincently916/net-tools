#!/usr/bin/env python

import socket,sys,argparse
parser = argparse.ArgumentParser(description="Port scanner")
parser.add_argument('--host',help='the server name or ip address')
parser.add_argument('--port', type=int,help='the port number to be checked')
args = parser.parse_args()
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = args.port 
host =  args.host

result = s.connect_ex((host,port))

if result == 0:
  print 'port ' + str(port) + ' is open'
else:
  print 'port ' + str(port) + ' is closed' 
