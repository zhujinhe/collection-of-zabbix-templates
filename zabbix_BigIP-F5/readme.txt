Template Device BigIP F5
Monitoring of F5 BigIP network load balancer. It uses SNMP items to monitor basic device parameters (CPU/RAM usage, hardware failure, global traffic) and also it discovers network interfaces, storage, virtual servers and pools. It requires manual addition of value mappings (Administration -> General -> Value Mapping)

F5 ltmPoolStatusAvailState  
0 - Pool Error (code
1 - Pool available (code
2 - Pool member(s) are currently not available (code
3 - Pool member(s) are down (code
4 - Pool availability is unknown (code
5 - Pool unlicensed (code


via https://github.com/thecamels/zabbix
需要在监控服务器创建上述mapping
需要在F5中设置System-SNMP-Agent-configuration中增加允许监控服务器的IP,System-SNMP-Agent-access(v1,v2c)中设置团体名
