
https://github.com/blacked/zbx_nginx_template
基于nginx status、access.log和zabbix trapper制作的模板，默认通过计划任务触发。

https://github.com/vicendominguez/nginx-zabbix-template
本文采用此种方式，在监控服务器上主动触发nginx的分析并入库。结合nginx-status模块和python分析结果加自定义命令。
方法1: zbx_nginx_agent_template.xml对应的是安装在被监控机上。结合zabbix-nginx.conf使用。
方法2: getNginxInfo.py部署在监控中心端，通过中心端调用脚本获取被监控服务器的值。

这2种方式针对nginx配置里白名单设置是不同的。方法1设置本机白名单，方法2设置监控中心端为白名单。

多条白名单分行写即可
                location =/nginx_status/ {
                      stub_status on;
                      access_log   off;
                      allow 127.0.0.1/32;
                      allow 123.57.143.102/32;
                      deny all;
                }
