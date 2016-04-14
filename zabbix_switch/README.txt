全局Macros默认团体名为public
如果需要修改需要在主机上设置为对应的团体名
Macro_key:{$SNMP_COMMUNITY}
Macro_value:自定义值

监控交换机大部分都是用的snmp配合lld（自动发现），但是zabbix2.4的lld不支持多个Multiple OID support in SNMP discovery。导致生成的模板可读性很差。所以以前业务线的交换机模板都没放到这里。
所以如果监控重点是交换机，建议升级为3.x
找不到的模板去这里找
http://monitoringartist.github.io/zabbix-searcher/#
https://share.zabbix.com/operating-systems/redhat-centos


