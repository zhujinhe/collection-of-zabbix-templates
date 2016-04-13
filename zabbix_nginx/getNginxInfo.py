#!/bin/env python
###  Vicente Dominguez
#
# Options:
#
# -a active 
# -a accepted
# -a handled 
# -a requests
# -a reading
# -a writting
# -a waiting
#


import urllib2, base64, sys, getopt
import re

##

def Usage ():
        print "Usage: getWowzaInfo.py -h 127.0.0.1 -P 80 -a [active|accepted|handled|request|reading|writting|waiting]"
        sys.exit(2)

##

def main ():

	# Default values
	host = "localhost"
	port = "80"
	getInfo = "None"

	if len(sys.argv) < 2:
		Usage()

	try:
        	opts, args = getopt.getopt(sys.argv[1:], "h:p:a:")
	except getopt.GetoptError:
                Usage()

	# Assign parameters as variables
	for opt, arg in opts :
		if opt == "-h" :
        		host = arg
	        if opt == "-p" :
        	        port = arg
	        if opt == "-a" :
        	        getInfo = arg

	url="http://" + host + ":" + port + "/nginx_status/"
	request = urllib2.Request(url)
	result = urllib2.urlopen(request)

	buffer = re.findall(r'\d{1,8}', result.read())

## Format:
## Active connections: 196
## server accepts handled requests
## 272900 272900 328835
## Reading: 0 Writing: 6 Waiting: 190

	if ( getInfo == "active"):
        	print buffer[0]
	elif ( getInfo == "accepted"):
		print buffer[1]
	elif ( getInfo == "handled"):
	        print buffer[2]
	elif ( getInfo == "requests"):
	        print buffer[3]
	elif ( getInfo == "reading"):
	        print buffer[4]
	elif ( getInfo == "writting"):
	        print buffer[5]
	elif ( getInfo == "waiting"):
	       	print buffer[6]
	else:
        	print "unknown"
	        sys.exit(1)

if __name__ == "__main__":
    main()
