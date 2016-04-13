#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import getopt, sys
from telnetlib import Telnet

# default memcached server to check
memcachedServer = '127.0.0.1'
memcachedPort = '11211'

ITEMS = (
    'bytes',
    'cmd_get',
    'cmd_set',
    'curr_items',
    'curr_connections',
    'limit_maxbytes',
    'uptime',
    'get_hits',
    'get_misses',
)

################################################################################
### This is based in Enrico Tröger sources from: 
###        http://www.pending.io/yet-another-zabbix-template-to-monitor-memcache/
### but I chose to make it with dictionaries instead of objects.
################################################################################
class MemcachedStatsReader(object):

    #----------------------------------------------------------------------
    def __init__(self, server, port):
        self._server = server
        self._port = port
        self._stats_raw = None
        self._stats = None

    #----------------------------------------------------------------------
    def read(self):
        self._read_stats()
        self._parse_stats()
        return self._stats

    #----------------------------------------------------------------------
    def _read_stats(self):
        connection = Telnet(self._server, self._port, timeout=30)
        connection.write('stats\n')
        connection.write('quit\n')
        self._stats_raw = connection.read_all()

    #----------------------------------------------------------------------
    def _parse_stats(self):
        self._stats = {}
        for line in self._stats_raw.splitlines():
            if not line.startswith('STAT'):
                continue
            parts = line.split()
            if not parts[1] in ITEMS:
                continue
	    index = parts[1]
	    self._stats[index] = parts[2]
        ratio = float (self._stats["get_hits"]) * 100 / float (self._stats["cmd_get"])
        self._stats["ratio"] = round (ratio, 2)

#----------------------------------------------------------------------

def Usage ():
        print "Usage: getMemcachedInfo.py -h 127.0.0.1 -p 11211 -a <item>"
        sys.exit(2)


def main(host, port):

    getInfo = "ratio"
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "h:p:a:")
        for opt,arg in opts:
		if opt  == '-h':
			host = arg			
		if opt == '-p':
			port = arg
		if opt == '-a':
			getInfo = arg		
    except:
	Usage()

    data = MemcachedStatsReader(host, port)
    items = data.read()
    try:
	    print items[getInfo]
    except: 
	    print "Not valid item."

if __name__ == '__main__':
    main(memcachedServer, memcachedPort)
