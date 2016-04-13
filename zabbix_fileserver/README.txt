说明:Template_app_FileServer可以监控磁盘的读写参数

使用:
Step1: 创建自定义参数,RPM安装的zabbix客户端可以在/etc/zabbix/zabbix_agentd.d/文件夹下新建文件名为userparameter_vfs.conf
[root@bjhrdb1 zabbix_agentd.d]# pwd 
/etc/zabbix/zabbix_agentd.d
[root@bjhrdb1 zabbix_agentd.d]# cat userparameter_vfs.conf 
UserParameter=custom.vfs.dev.read.ops[*],cat /proc/diskstats | grep sda | head -1 |awk '{print $4}'
UserParameter=custom.vfs.dev.read.ms[*],cat /proc/diskstats | grep sda | head -1 | awk '{print $$7}'
UserParameter=custom.vfs.dev.write.ops[*],cat /proc/diskstats | grep sda | head -1 | awk '{print $$8}'
UserParameter=custom.vfs.dev.write.ms[*],cat /proc/diskstats | grep sda | head -1 | awk '{print $$11}'
UserParameter=custom.vfs.dev.io.active[*],cat /proc/diskstats | grep sda | head -1 | awk '{print $$12}'
UserParameter=custom.vfs.dev.io.ms[*],cat /proc/diskstats | grep sda | head -1 | awk '{print $$13}'
UserParameter=custom.vfs.dev.read.sectors[*],cat /proc/diskstats | grep sda | head -1 | awk '{print $$6}'
UserParameter=custom.vfs.dev.write.sectors[*],cat /proc/diskstats | grep sda | head -1 | awk '{print $$10}'

Step2: 重启zabbix_agent:
/etc/init.d/zabbix-agent restart

Step3: 在zabbix server web interface中的主机中Link此模板.
