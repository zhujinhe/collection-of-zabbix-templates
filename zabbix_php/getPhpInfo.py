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

import simplejson as json
import urllib2, base64, sys, getopt
import re

##

def Usage ():
        print("Usage: getPhpInfo.py -h 127.0.0.1 -P 80 -a [active|accepted|handled|request|reading|writing|waiting]")
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

    url="http://" + host + ":" + port + "/php-fpm_status?json"
    request = urllib2.Request(url)
    try:
        result = urllib2.urlopen(request)
        buffer = json.loads(result.read())
    except:
        print("-1")
        sys.exit(1)
    print(buffer.pop(getInfo,'unknown'))
    sys.exit(0)

if __name__ == "__main__":
    main()
