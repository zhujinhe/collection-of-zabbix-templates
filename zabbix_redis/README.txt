1.配置Zabbix客户端
默认zabbix_agentd配置文件位置为：/etc/zabbix/zabbix_agentd.d/
修改userparameter_redis.conf中的路径端口为实际地址。然后zabbix_agentd服务。service zabbix_agentd restart
2.在服务器端导入模板：zbx_redis_6379.xml。此模板默认端口为6379

说明:
可用宏
{$REDIS_PORT}: redis端口号
{$REDIS_LIST_KEY}:查询当前队列数量
查询当前队列实例用法:
zabbix_get -s ip -k redis_LLEN[{$REDIS_PORT},{$REDIS_LIST_KEY}]
解析为:
zabbix_get -s ip -k redis_LLEN[6379,bid:record:queue]
