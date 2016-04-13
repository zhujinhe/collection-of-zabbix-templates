通过zabbix监控VMWare
官方配置文档:https://www.zabbix.com/documentation/2.4/manual/vm_monitoring
VMware_keys手册:https://www.zabbix.com/documentation/2.4/manual/config/items/itemtypes/simple_checks/vmware_keys

配置VMware监控简要步骤:
1.zabbix server中开启VMWare
compile zabbix server with required options (--with-libxml2 and --with-libcurl)
set the StartVMwareCollectors option in Zabbix server configuration file to 1 or more

vim /etc/zabbix/zabbix_server.conf
# StartVMwareCollectors=0
StartVMwareCollectors=24

2.VMware中配置账号和权限，比如新增本地账号zabbix，密码zabbix，然后在VMware中赋予只读权限。

3.创建主机，配置Host configuration

To use VMware simple checks the host must have the following user macros defined:
{$URL} - VMware service (vCenter or ESX hypervisor) SDK URL (https://servername/sdk).
{$USERNAME} - VMware service user name
{$PASSWORD} - VMware service {$USERNAME} user password

4.链接主机和Template virt VMware（只需要这1个）
Link the host to the VMware service template
Click on the Add button to save the host

说明：
1. Template virt VMware配置了LLD，自动发现的VMware宿主机会链接到Template Virt VMware Hypervisor，自动发现的虚拟机会链接到Template Virt VMware Hypervisor
2. 默认的模板中只配置了items，并未配置trigger，需要按照VMware_Keys手册的定义设置报警。

遇见的错误:
1.zabbix-server异常退出，查看/var/log/zabbix/zabbix_server.log中提示:
16149:20150505:121412.298 [file:vmware.c,line:79] zbx_mem_malloc(): out of memory (requested 512 bytes)
16149:20150505:121412.298 [file:vmware.c,line:79] zbx_mem_malloc(): please increase VMwareCacheSize configuration parameter
解决方法:
修改/etc/zabbix/zabbix_server.conf中VMwareCacheSize256K-2G
# VMwareCacheSize=8M
VMwareCacheSize=128M
重启zabbix-server
/etc/init.d/zabbix-server restart

