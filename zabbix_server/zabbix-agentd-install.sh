#!/bin/bash
# install zabbix-agent 
# Autor:zhujh2
# Date:20150126
# more information: https://www.zabbix.com/documentation/2.4/manual/installation/install_from_packages
#                   http://blog.chinaunix.net/uid-11121450-id-3310064.html
  
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

zabbix_server_ip="172.16.0.136, 172.27.4.142, 10.12.1.21";
LocalIP=`/sbin/ifconfig -a|grep inet|grep -v inet6|awk '{print $2}'|tr -d "addr:" | grep 172|head -n 1`;
system_version=`grep -o -P '(?=\d\.\d+)\d' /etc/issue`;
platform=`uname -p`;
zabbix_release_URL="http://repo.zabbix.com/zabbix/2.4/rhel/${system_version}/${platform}/zabbix-release-2.4-1.el${system_version}.noarch.rpm"
echo $zabbix_release_URL

function ChkSystem()
{
  grep -qE "CentOS|Red" /etc/issue
  if [ $? -ne 0 ]; then
  echo "This scripts only runs on Red Hat OR CentOS"
  fi
}

function ChkNetwork()
{
  if [ `curl -I -m 10 -o /dev/null -s -w %{http_code} $zabbix_release_URL` != "200" ]; then 
    echo "Network unreachable,try using proxy";
    export http_proxy="http://172.16.0.108:8888/"
    export ftp_proxy="http://172.16.0.108:8888/"
    use_proxy=1
    if [ `curl -I -m 10 -o /dev/null -s -w %{http_code} $zabbix_release_URL` != "200" ]; then 
      echo "Network unreachable,Installation has been canceled.Please check your network and DNS setting."
      exit 1
    fi
  else
    echo "Network is available."
  fi
}

ChkSystem;
ChkNetwork;
wget ${zabbix_release_URL} -O zabbix-release-2.4.1.rpm
rpm -Uvh zabbix-release-2.4.1.rpm;
yum install -y zabbix-agent --nogpgcheck;

sed -i "s/Server=127.0.0.1/Server=$zabbix_server_ip/g" /etc/zabbix/zabbix_agentd.conf 
sed -i "s/Hostname=Zabbix server/Hostname=$HOSTNAME/g" /etc/zabbix/zabbix_agentd.conf 
chkconfig zabbix-agent on
/etc/init.d/zabbix-agent restart

# script below is non-essential. 
if [ -n "$http_proxy" ] ;then
  unset http_proxy
  unset ftp_proxy
  echo "http_proxy unset success"
fi
