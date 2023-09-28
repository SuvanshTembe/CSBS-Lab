#!/bin/python3

from datetime import datetime as dt
import sys
import socket 

#Defining our target

if len(sys.argv) == 2:
	  target = socket.gethostbyname(sys.argv[1]) #translates hostname to IP
else:							#argv 0 is port_scanner.py & argv 1 is ip
	print("Invalid number of arguments given")
	print('syntax: python3 port_scanner.py i<p>')
	
#Adding a pretty Banner
	
print( '-' * 50)
print('Scanning started' +target)
print('Time Started since'+str(dt.now()))	
print( '-' * 50)
	
#Connecting to Ports
try:
	for PORT in range (1,65535):
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			result  = s.connect_ex((target,PORT))
			if result == 0:
			        print("PORT {} is open".format(PORT) )
			s.close()
			

except KeyboardInterrupt:
		 print("\n Exiting program ")
		 sys.exit()
except socket.gaierror:
		print(' Hostname could not be resolved ')
		sys.exit()
except socket.error:
		print("\n Couldn't connect to server")
		sys.exit()
			
