1.配置Zabbix客户端
默认zabbix_agentd配置文件位置为：/etc/zabbix/zabbix_agentd.d/
编辑redis_lld.txt的redis IP和端口号,并把次文件放在/etc/zabbix/ (和userparameter_redis_lld.conf对应即可)
然后重启zabbix_agentd服务 service zabbix_agentd restart
2.在服务器端导入模板：zbx_redis_lld.xml。

说明:
可用宏
{#REDIS_IP}: redis IP地址
{#REDIS_PORT}: redis端口号
{$REDIS_LIST_KEY}:查询当前队列数量
查询当前队列实例用法:
zabbix_get -s ip -k redis_LLEN[{$REDIS_PORT},{$REDIS_LIST_KEY}]
解析为:
zabbix_get -s ip -k redis_LLEN[6379,bid:record:queue]

这个模板需要注意的地方:
1、该模板为自动发现模板，当修改模板的时候，扫描出新的items会当做是新的而不是替换。旧的会在自动发现key的Keep lost resources period (in days)值后删除，也可手动删除。
2、编辑redis_lld.txt的时候注意格式。
