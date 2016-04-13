"""
  zabbix python api get Unacknowledged issue
"""

from getpass import getpass
from pyzabbix import ZabbixAPI

# The hostname at which the Zabbix web interface is available
ZABBIX_SERVER = 'http://172.16.0.136/zabbix'

zapi = ZabbixAPI(ZABBIX_SERVER)

# Login to the Zabbix API
zapi.login('Admin', 'nidemima')

# Get a list of Unacked issues
triggers = zapi.trigger.get(only_true=1,
    skipDependent=1,
    monitored=1,
    active=1,
    output='extend',
    expandDescription=1,
    expandData='host',
    withLastEventUnacknowledged=1,
    selectGroups='extend',
    selectHosts='extend',
)

# Print a list containing only "Unacked" triggers
for t in triggers:
    if int(t['value']) == 1:
        groupList = []
        hostList = []
        for selectGroup in t['groups']:
            groupList.append(selectGroup['name'])
        for selectHost in t['hosts']:
            hostList.append(selectHost['host'])

        print "Groups:",', '.join(groupList), "hostname:", t['hostname'], "Interface:", ', '.join(hostList), "description:", t['description']
