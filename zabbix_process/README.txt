zabbix除了可以自定义监控项外,还可以监控指定的进程

Zabbix agent中proc.mem[<name>,<user>,<mode>,<cmdline>]和proc.num[<name>,<user>,<state>,<cmdline>]

参考文章:
https://www.zabbix.com/documentation/2.4/manual/config/items/itemtypes/zabbix_agent
http://www.2cto.com/os/201405/302249.html


摘要:

proc.mem[<name>,<user>,<mode>,<cmdline>]
功能:用户进程消耗的内存	
返回值:内存使用量 (字节单位).
参数:name – 进程名 (默认值 “all processes”)user – 用户名 (默认值“all users”)mode – 可选值: avg, max, min, sum (默认) cmdline – 命令行过滤(正则表达时)
描述:示例keys:proc.mem[,root]– root的进程消耗了多少内存 proc.mem[zabbix_server,zabbix] – zabbix用户运行的zabbix_server使用了多少内存 proc.mem[,oracle,max,oracleZABBIX] – memory used by the most memory-hungry process running under oracle having oracleZABBIX in its command line

proc.num[<name>,<user>,<state>,<cmdline>]
功能:某用户某些状态的进程的数量	
返回值:进程数量
参数:name – 进程名称 (默认“all processes”)user – 用户名 (默认 “all users”)state – 可用值: all (默认), run,sleep, zomb cmdline – 命令行过滤(正则表达时)
描述:示例keys: proc.num[,mysql]– MySQL用户运行的进程数量proc.num[apache2,www-data] – www-data运行了多少个apache2进程proc.num[,oracle,sleep,oracleZABBIX] – number of processes in sleep state running under oracle having oracleZABBIX in its command line 备注：Windows系统只支持name和user两个参数
例如:zabbix_get -s 10.12.7.18 -k proc.num[,root,,ehomepay_SmsKernel-0.0.1-SNAPSHOT.jar]
输出结果为1,代表有1个命令行中包含ehomepay_SmsKernel-0.0.1-SNAPSHOT.jar的进程.

On Windows, only the name and user parameters are supported.
proc.num[<name>,<user>] name和user不区分大小写
proc.num[SoftphoneService.exe,SYSTEM]

Template Process Windows模板中带有4个监控项,每个监控项对应主机上的一对宏(需要在主机上配置):
{$WINPROCNAME1}
{$WINPROCUSER1}
{$WINPROCNAME2}
{$WINPROCUSER2}
{$WINPROCNAME3}
{$WINPROCUSER3}
{$WINPROCNAME4}
{$WINPROCUSER4}
监控主机的方法:主机上关联Template Process Windows模板,并增加对应的宏即可完成监控.如果连续2此监控进程数量为0则报警.
其中{$WINPROCNAMEN}对应进程名称,{$WINPROCUSERN}对应进程的用户.

另外一个常用的windows监控items是service_state[service]:https://www.zabbix.com/documentation/2.4/manual/config/items/itemtypes/zabbix_agent/win_keys
