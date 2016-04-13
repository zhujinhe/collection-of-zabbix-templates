使用zabbix监控oracle,从网上搜索大概有3种方法
通过odbc监控oracle:
官方:https://www.zabbix.com/documentation/2.4/manual/config/items/itemtypes/odbc_checks
博客:http://habrahabr.ru/post/226365/
通过orabbix:这个文章较多
http://www.zabbix.org.cn/viewtopic.php?f=19&t=36
通过Pyora:
http://bicofino.io/blog/2013/12/09/monitoring-oracle-with-zabbix/

采用Pyora监控步骤:
第一步:服务器端安装pyora:

参考http://leigh.cudd.li/article/Setting_up_cxOracle_on_CentOS_6
从oracle官方网站下载对应系统和版本的rpm包,本例为Centox 6.x:
oracle-instantclient11.2-basic-11.2.0.3.0-1.x86_64.rpm
oracle-instantclient11.2-devel-11.2.0.3.0-1.x86_64.rpm
oracle-instantclient11.2-sqlplus-11.2.0.3.0-1.x86_64.rpm
rpm -ivh oracle-instantclient11.2-basic-11.2.0.3.0-1.x86_64.rpm oracle-instantclient11.2-devel-11.2.0.3.0-1.x86_64.rpm oracle-instantclient11.2-sqlplus-11.2.0.3.0-1.x86_64.rpm
echo "/usr/lib/oracle/11.2/client64/lib" >>/etc/ld.so.conf.d/oracle.conf
ldconfig
wget http://hivelocity.dl.sourceforge.net/project/cx-oracle/5.1.1/cx_Oracle-5.1.1.tar.gz
tar xvfz cx_Oracle-5.1.1.tar.gz
cd cx_Oracle-5.1.1
ORACLE_HOME=/usr/lib/oracle/11.2/client64/ python setup.py build
ORACLE_HOME=/usr/lib/oracle/11.2/client64/ python setup.py install
如果提示error: command 'gcc' failed with exit status 1 需要安装 gcc python-devel
[root@MOp_zbx01 cx_Oracle-5.1.1]# yum install gcc python-devel
测试:python -c 'import cx_Oracle'
如果没有错误提示则表示安装成功.
安装yum install -y python-argparse

第二步:在web中导入模板,并配置interface/宏/模板等信息.
宏格式如下(值需要按照实际情况填写):
{$ADDRESS} 192.168.0.1 
{$DATABASE} MY_ORACLE_DATABASE 
{$USERNAME} ZABBIX 
{$PASSWORD} ZABBIX 
{$ARCHIVE} VGDATA
{$HIGH}   90
({$HIGH}是自动发现表空间利用率的报警)

更改对应items的oracle相关pyora开头的items的接口为127.0.0.1:10050
为了使oracle支持自动发现,需要更新Discovery rules里的的接口地址:Discovery  Oracle tablespaces, Discovery Oracle temp tablespaces, Discovery Oracle ASM volumes为127.0.0.1:10050
Item prototypes中的Item prototypes的Host Interface改为127.0.0.1:10050
安装成功后参考通过pyora的文章进行监控即可.需要非常注意的地方是,示例中的监控使用的是zabbix server这个机器的zabbix_agentd进行的监控,因此Agent Interface应该有127.0.0.1:10050,并把在configuration-host中将oracle相关的items的interface修改为127.0.0.1:10050, 如果有其他的需要被监控端执行的监控项,则可以通过被监控端IP:10050的interface进行监控.

第三部:在被监控的oracle里创建账号, 并赋予相应的权限(下面脚本中的<REPLACE WITH PASSWORD>改为对应的密码如ZABBIX)

CREATE USER ZABBIX IDENTIFIED BY <REPLACE WITH PASSWORD> DEFAULT TABLESPACE SYSTEM TEMPORARY TABLESPACE TEMP PROFILE DEFAULT ACCOUNT UNLOCK;
GRANT CONNECT TO ZABBIX;
GRANT RESOURCE TO ZABBIX;
ALTER USER ZABBIX DEFAULT ROLE ALL;
GRANT SELECT ANY TABLE TO ZABBIX;
GRANT CREATE SESSION TO ZABBIX;
GRANT SELECT ANY DICTIONARY TO ZABBIX;
GRANT UNLIMITED TABLESPACE TO ZABBIX;
GRANT SELECT ANY DICTIONARY TO ZABBIX;
GRANT SELECT ON V_$SESSION TO ZABBIX;
GRANT SELECT ON V_$SYSTEM_EVENT TO ZABBIX;
GRANT SELECT ON V_$EVENT_NAME TO ZABBIX;
GRANT SELECT ON V_$RECOVERY_FILE_DEST TO ZABBIX;

