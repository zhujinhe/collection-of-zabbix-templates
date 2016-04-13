插件地址:
https://github.com/gpmidi/zabbix-apache-stats

此插件需要依赖zabbix-sender, 通过自定义参数, zabbix-sender配合zabbix trapper这种类型的item实现数据的汇报。
默认是通过定义1个普通item,这个item调用的时候附带执行sender内容，也可以使用计划任务触发sender过程。

备注:
zabbix trapper与zabbix agent(active)不是同一种。
git中的默认路径该改为/etc/zabbix/zabbix_agentd.conf
