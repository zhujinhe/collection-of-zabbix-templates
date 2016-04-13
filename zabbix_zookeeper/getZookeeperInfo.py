#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import getopt, sys
from telnetlib import Telnet

# default Zookeeper server to check
ZookeeperServer = '127.0.0.1'
ZookeeperPort = 2181
ZookeeperCommand = 'mntr'
ZookeeperKey = 'zk_version'

# ZooKeeper Commands: The Four Letter Words 
# Referer: http://zookeeper.apache.org/doc/r3.4.6/zookeeperAdmin.html#sc_zkCommands

CommandKey={
'conf':['clientPort','dataDir','dataLogDir','tickTime','maxClientCnxns','minSessionTimeout','maxSessionTimeout','serverId','initLimit','syncLimit','electionAlg','electionPort','quorumPort','peerType'],
'ruok':['state'],
'mntr':['zk_version','zk_avg_latency','zk_max_latency','zk_min_latency','zk_packets_received','zk_packets_sent','zk_num_alive_connections','zk_outstanding_requests','zk_server_state','zk_znode_count','zk_watch_count','zk_ephemerals_count','zk_approximate_data_size','zk_open_file_descriptor_count','zk_max_file_descriptor_count','zk_followers','zk_synced_followers','zk_pending_syncs']
}

class ZooKeeperCommands(object):
    #----------------------------------------------------------------------
    def __init__(self,server,port,zkCommand,zkKey):
        self._server = server
        self._port = port
        self._zkCommand = zkCommand
        self._zkKey = zkKey
        self._value_raw = None
        self._value = None 

    def zkExec(self):
        self._exec_command()
        self._parse_value()
        return self._value
    
    def _exec_command(self):
        tn = Telnet(self._server, self._port, timeout=30)
        # tn.read_until('login: ')
        # tn.write(username + '\n')
        # tn.read_until('password: ')
        # tn.write(password + '\n')
        # tn.read_until(finish)
        tn.write('%s\n' % self._zkCommand)
#        tn.write('conf\n')
        tn.write('quit\n')
        self._value_raw = tn.read_all()
#        print type(self._value_raw)
#        print (self._value_raw)

    def _parse_value(self):
        self._value = {}
        if self._zkCommand == 'mntr':
            for line in self._value_raw.splitlines():
                parts = line.split('	')
                index = parts[0]
                self._value[index] = parts[1]
        elif self._zkCommand == 'conf':
            for line in self._value_raw.splitlines():
                parts = line.split('=')
                index = parts[0]
                self._value[index] = parts[1]
        elif self._zkCommand == 'ruok':

            if self._value_raw == 'imok':
                self._value['state'] = 1
#                print " server is running in a non-error state."
            else:
                self._value['state'] = 0
#                print "ruok command does not respond at all"
        else:
            "zkCommand is wrong"

###########################################################################################################

def Usage():
        print '''
Usage:
    getZookeeperInfo.py -h 127.0.0.1 -p 2181 -c <zkCommand> -k <zkKey>"
    getZookeeperInfo.py --host 127.0.0.1 --port 2181 --zkCommand <zkCommand> --zkKey <zkKey>
    '''
        for key in CommandKey:
            print 'zkCommand:%s, zkKey:%s' %(key, CommandKey[key])

###########################################################################################################

def main(host, port, zkCommand, zkKey):

    try:
        options, args = getopt.getopt( sys.argv[1:], "h:p:c:k:", ["host=","port=","zkCommand=","zkKey="]);
        for name,value in options:
            if name in ('-h','--host'):
                host = value
            if name in ('-p','--port'):
                port = value
            if name in ('-c','--zkCommand'):
                zkCommand = value
            if name in ('-k','--zkKey'):
                zkKey = value
    except getopt.GetoptError, err:  
        print str(err)
        Usage()
        sys.exit(1)

    
    data = ZooKeeperCommands(host, port, zkCommand, zkKey)
    items = data.zkExec()
    try:
        print items[zkKey]
    except: 
        print "Not valid item."
        Usage()
if __name__ == '__main__':
    main(ZookeeperServer, ZookeeperPort,ZookeeperCommand,ZookeeperKey)
