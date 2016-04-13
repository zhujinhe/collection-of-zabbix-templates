通过zabbix监控php-fpm状态:

步骤1.开启php-fpm状态查询
;pm.status_path = /status 改为
pm.status_path = /php-fpm_status

步骤2.配置nginx
在默认server块中增加如下内容
        location /php-fpm_status {
            include fastcgi_params;
            fastcgi_pass 127.0.0.1:9000;
            fastcgi_param SCRIPT_FILENAME $fastcgi_script_name;
        }
步骤3.重启nginx和php-fpm
service nginx restart
service php-fpm restart
4. 打开status页面
http://IP/php-fpm_status
pool:                 www
process manager:      dynamic
start time:           14/May/2014:22:40:15 +0800
start since:          58508
accepted conn:        33
listen queue:         0
max listen queue:     8
listen queue len:     0
idle processes:       2
active processes:     1
total processes:      3
max active processes: 5
max children reached: 0
slow requests:        2091
名词解释:
pool – fpm池子名称，大多数为www
process manager – 进程管理方式,值：static, dynamic or ondemand. dynamic
start time – 启动日期,如果reload了php-fpm，时间会更新
start since – 运行时长
accepted conn – 当前池子接受的请求数
listen queue – 请求等待队列，如果这个值不为0，那么要增加FPM的进程数量
max listen queue – 请求等待队列最高的数量
listen queue len – socket等待队列长度
idle processes – 空闲进程数量
active processes – 活跃进程数量
total processes – 总进程数量
max active processes – 最大的活跃进程数量（FPM启动开始算）
max children reached – 大道进程最大数量限制的次数，如果这个数量不为0，那说明你的最大进程数量太小了，请改大一点。
slow requests – 启用了php-fpm slow-log，缓慢请求的数量

参考文档:http://www.ttlsa.com/php/use-php-fpm-status-page-detail/

道理是这样的，模板是比这https://github.com/vicendominguez/nginx-zabbix-template写的。
这个模板也可以考虑改成trapper+sender的方式。
或者是shell的方式https://github.com/maxvgi/zabbix-templates/tree/master/php-fpm

