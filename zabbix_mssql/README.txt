参考地址:
MS SQL模板:https://github.com/artos220/zabbix_mssql_template
Freetds官方网站:http://www.freetds.org/
测试freetds是否能连mssql:http://blog.csdn.net/aidenliu/article/details/6664382
数据库与TDS版本:http://www.freetds.org/userguide/choosingtdsprotocol.htm#TAB.PROTOCOL.BY.PRODUCT
Recommended UnixODBC settings for most popular databases:https://support.zabbix.com/browse/ZBX-6839
http://www.cerebralmastication.com/2013/01/installing-debugging-odbc-on-mac-os-x/

How The pieces fit together:
interface <=> unixODBC <=> FreeTDS <=> MS SQL
                (isql)      (tsql)          

freetds安装:
./configure --enable-msdblib --with-tdsver=7.2
make
make install
通过tsql  -C查看状态
make过程会显示lib目录位置:/usr/local/lib
/usr/local/lib/libtdsodbc.so

安装完毕编辑文件:
# /etc/odbcinst.ini 增加
[FreeTDS]
Dirver		= /usr/local/lib/libtdsodbc.so.0
Setup 		= /usr/lib64/libtdsS.so
UsageCount	= 1

# /etc/odbc.ini 增加
[BJ-CALL-CIC002]
Driver  = FreeTDS
ServerName      = BJ-CALL-CIC002

# /usr/local/etc/freetds.conf 增加
# HOMELINK Microsoft SQL server 2008 for BJ-CALL-CIC002 added by zhujh2
[BJ-CALL-CIC002]
	host = 172.16.5.152
	port = 1433
	tds version = 7.2

测试是否成功:
执行:tsql -S BJ-CALL-CIC002 -U zabbix -P zabbix
或者:TDSVER=8.0 tsql -H 172.16.5.152 -p 1433 -U zabbix -P zabbix
备注:tds version为7.2有时会显示Error 100 (severity 11):unrecognized msgno(可能是BUG)

1> select @@version
2> go

Microsoft SQL Server 2008 R2 (RTM) - 10.50.1617.0 (Intel X86) 
	Apr 22 2011 11:57:00 
	Copyright (c) Microsoft Corporation
	Enterprise Edition on Windows NT 5.2 <X86> (Build 3790: Service Pack 2)

(1 row affected)

如果新增监控机器,需要
1:编辑/etc/odbc.ini和/usr/local/etc/freetds.conf文件(待测试是否是必须)
2:Link Template App MSSQL Server模板到主机
