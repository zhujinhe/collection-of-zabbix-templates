Windows:
功能:输出ping某个IP地址的丢包率,并通过zabbix进行检测.

步骤:
增加检测脚本
c:\Program Files\zabbix\PingCheck.bat
@echo off
::filename:PingCheck.bat
::%1 is the first parameter of the script.
::CLIUsage:PingCheck.bat 10.10.10.14
setlocal enabledelayedexpansion
for /f "tokens=1,2 delims=(%%" %%a in ('ping -n 3 %1^|find "%%"') do (
   if not defined packet_loss_rate set packet_loss_rate=%%b
)
set /a rate=!packet_loss_rate!+0
echo %rate%

zabbix-agent配置自定义参数:C:\Program Files\zabbix\confzabbix_agentd.win.conf增加如下行
UserParameter=hl.pingcheck[*],c:\"Program Files"\zabbix\PingCheck.bat $1

在zabbix server web界面中新建Template Windows Heartbeat模板,并配置items.
Type:Zabbix agent
Key:hl.pingcheck[{$WINPINGCHECKIP1}]

被监控主机链接到模板Template Windows Heartbeat,并增加如下宏.
{$WINPINGCHECKIP1}
{$WINPINGCHECKIP2}
{$WINPINGCHECKIP2}
当丢包率不为0的时候则会报警.

=======================================
Centos:
yum install -y heartbeat
检测heartbeat状态的参考:https://www.zabbix.com/forum/showthread.php?t=9121
#/bin/bash
# 0 is bad, 1 is good
STAT=`/usr/bin/cl_status rscstatus`
#echo $STAT
if [ "$STAT" = "all" ] || [ "$STAT" = "local" ]; then
  echo 1
else
  echo 0
fi

参考文章:
Current Heartbeat Manual pages: http://www.linux-ha.org/doc/man-pages/re-clstatus.html
heartbeat(8) - Linux man page: http://linux.die.net/man/8/heartbeat
Getting Started with Linux-HA (heartbeat):http://www.snrg.cs.hku.hk/srg/html/cprobe/ha/GettingStarted.html
http://www.linuxjournal.com/article/9838
http://serverfault.com/questions/333853/heartbeat-find-out-machines-status-within-a-cluster

备注:此项检查不同于Simple check中的icmpping[<target>,<packets>,<interval>,<size>,<timeout>].
icmpping是检测zabbix server通过ping对象的IP地址来确认对象的存活状态,常用来监控网络打印机、宽带的公网网关地址、网络监控设备、不支持SNMP的交换机和无线路由器、无法安装客户端的电脑等,将监控最大化的横向扩展.而本例中则是通过zabbix-agent检测主机A和B的ping丢包率.
