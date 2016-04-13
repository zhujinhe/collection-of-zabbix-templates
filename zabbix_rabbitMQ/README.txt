使用的模板是https://github.com/jasonmcintosh/rabbitmq-zabbix
https://github.com/zhujinhe/rabbitmq-zabbix

这个模板需要在/etc/zabbix/scripts/rabbitmq文件夹下新建.rab.auth。并设置为可执行权限，用于shell中读取变量值。
这个模板中的items很多是使用Zabbix agent (active)模式。需要在agent的配置文件中配置主动地址。


需要注意的地方:
服务器在启动rabbitmq之后如果更换过主机名，需要手动指定HOSTNAME和NODE名字。否则会提示urllib2.URLError: <urlopen error [Errno -2] Name or service not known>。
示例
$ cat /etc/zabbix/scripts/rabbitmq/.rab.auth
USERNAME=guest
PASSWORD=guest
CONF=/etc/zabbix/zabbix_agentd.conf
HOSTNAME=jiqiming
NODE=rabbit@jiqiming

模板默认的配置文件位置不对
/etc/zabbix/zabbix_agentd.conf 不是/etc/zabbix/zabbix_agent.conf

需要补充@rabbitmq vhosts for discovery才能启动自动发现
