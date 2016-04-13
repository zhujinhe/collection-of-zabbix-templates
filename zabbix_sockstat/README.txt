参考文章:
安装方法:https://systembash.com/track-tcp-and-udp-connections-with-zabbix/
关于sockstat的介绍:http://blog.csdn.net/zdwzzu2006/article/details/7753495
简述:
被监控端Add the following parameters to zabbix_agentd.conf(通常在/etc/zabbix/):
或者在/etc/zabbix/zabbix_agentd.d/新建userparameter_sockstat.conf:
UserParameter=sockstat.sockets,cat /proc/net/sockstat|grep sockets|cut -d' ' -f 3
UserParameter=sockstat.tcp.inuse,cat /proc/net/sockstat|grep TCP|cut -d' ' -f 3
UserParameter=sockstat.tcp.orphan,cat /proc/net/sockstat|grep TCP|cut -d' ' -f 5
UserParameter=sockstat.tcp.timewait,cat /proc/net/sockstat|grep TCP|cut -d' ' -f 7
UserParameter=sockstat.tcp.allocated,cat /proc/net/sockstat|grep TCP|cut -d' ' -f 9
UserParameter=sockstat.tcp.mem,cat /proc/net/sockstat|grep TCP|cut -d' ' -f 11
UserParameter=sockstat.udp.inuse,cat /proc/net/sockstat|grep UDP:|cut -d' ' -f 3
UserParameter=sockstat.udp.mem,cat /proc/net/sockstat|grep UDP:|cut -d' ' -f 5
重启zabbix-agent
/etc/init.d/zabbix-agent restart

注释:如果selinux开启的话,这种方式会碰到权限问题:
[root@FWTp_Ngx01 zabbix_agentd.d]# getenforce 
Enforcing
cat: /proc/net/sockstat: Permission denied
[root@FWTp_Ngx01 zabbix_agentd.d]# which cat
/bin/cat
[root@FWTp_Ngx01 zabbix_agentd.d]# ll /bin/cat 
-rwxr-xr-x. 1 root root 48568 Nov 22  2013 /bin/cat
[root@FWTp_Ngx01 zabbix_agentd.d]# ll /proc/net/sockstat
-r--r--r--. 1 root root 0 Feb 26 11:46 /proc/net/sockstat

监控服务器导入模板,并link到主机上.

在此文章上作出的修改:
模板中加宏和报警
{$TCP_TIMEWAIT_THRESHOLD}=>1000
{$TCP_ALLOCATED_THRESHOLD}=>1000
修改图形模板中的INUSE为ALLOCATED

如何自定义这些报警阈值:{$TCP_ALLOCATED_THRESHOLD} is defined on template macros and host macros(Mandatory:NO,High weight)
修改模板阈值:Configuration-Templates-TCP/UDP status-Macros修改
修改某主机阈值:找到主机-Macros里增加值{$TCP_TIMEWAIT_THRESHOLD}:自定义值,{$TCP_ALLOCATED_THRESHOLD}:自定义值
