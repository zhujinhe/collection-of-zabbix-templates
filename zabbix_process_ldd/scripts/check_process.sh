#!/bin/bash
#
ps -ef > /etc/zabbix/scripts/ps.log
#Process_num=`ps auxf|grep -v grep|grep -c "$1"`
Process_num=`cat /etc/zabbix/scripts/ps.log|grep -v grep|grep -v "check_process.sh"|grep -c "$1"`
echo $Process_num
