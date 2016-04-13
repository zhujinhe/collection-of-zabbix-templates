0.在mysql中配置zabbix账号并赋权.
mysql> grant usage on `mysql`.* TO 'zabbix'@'localhost' identified by 'zabbix' with grant option;
Query OK, 0 rows affected (0.00 sec)
mysql> grant usage on `performance_schema`.* to 'zabbix'@'localhost' identified by 'zabbix' with grant option;
Query OK, 0 rows affected (0.00 sec)
mysql> flush privileges;
Query OK, 0 rows affected (0.00 sec)
检查权限
mysql> show grants for zabbix@localhost;
+---------------------------------------------------------------------------------------------------------------+
| Grants for zabbix@localhost                                                                                   |
+---------------------------------------------------------------------------------------------------------------+
| GRANT USAGE ON *.* TO 'zabbix'@'localhost' IDENTIFIED BY PASSWORD '*DEEF4D7D88CD046ECA02A80393B7780A63E7E789' |
| GRANT USAGE ON `mysql`.* TO 'zabbix'@'localhost' WITH GRANT OPTION                                            |
| GRANT USAGE ON `performance_schema`.* TO 'zabbix'@'localhost' WITH GRANT OPTION                               |
+---------------------------------------------------------------------------------------------------------------+
3 rows in set (0.00 sec)
退出mysql
mysql>exit;
1.Zabbix客户端修改：RPM安装的zabbix_agentd配置文件默认位置为：/etc/zabbix/zabbix_agentd.d/
修改userparameter_mysql.conf中的mysql路径为实际环境中的路径，然后zabbix_agentd服务。service zabbix_agentd restart
2.服务器端模板使用zabbix2.4.x自带的mysql模板zbx_export_templates.xml即可。
4.确保selinux是关闭状态(setenforce 0)或者放行(方法待补充),否则会提示类似sh: /usr/local/mysql-5.6/bin/mysql: Permission denied

说明:以UserParameter=mysql.ping,HOME=/var/lib/zabbix /usr/local/mysql-5.6/bin/mysqladmin -uzabbix -pzabbix ping 2>/dev/null | grep -c alive为例
一种配置方法为:UserParameter=mysql.ping,HOME=/var/lib/zabbix mysqladmin ping | grep -c alive
并配合设置完数据库帐户之后在被监控端新建/var/lib/zabbix/.my.cnf以提供Zabbix Agent访问数据库，内容类似如下：
# Zabbix Agent
  [mysql]
  host     = localhost
  user     = zabbix
  password = 密码
  socket   = /path/to/your/mysqld.sock
  [mysqladmin]
  host     = localhost
  user     = zabbix
  password = 密码
  socket   = /path/to/your/mysqld.sock
另外一种配置方法只写为:UserParameter=mysql.ping,/usr/local/mysql-5.6/bin/mysqladmin -uzabbix -pzabbix ping 2>/dev/null | grep -c alive


模板中增加针对从库查看复制状态：(默认并未开启)
首先，数据库赋予查询状态的权限。
mysql> grant replication client on *.* to 'zabbix'@'localhost' identified by 'zabbix' with grant option;
mysql> flush privileges;
然后userparameter_mysql.conf中增加
UserParameter=mysql.slave[*],echo "show slave status\G;" | HOME=/var/lib/zabbix /usr/local/mysql/bin/mysql -uzabbix -pzabbix 2>/dev/null |awk '/$1:/{print $$2}'
最后在zabbix模板中增加如mysql.status[Slave_IO_Running]等项目,然后在主机中连接到此模板，并将MySQL Slave的3个监控项启用(enable)
