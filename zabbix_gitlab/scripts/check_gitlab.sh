#!/bin/bash
#
#GIT_servers="gitlab-workhorse
#logrotate
#postgresql
#redis
#registry
#sidekiq
#unicorn"

#for i in $GIT_servers;do
#    if [ `sudo gitlab-ctl status|grep $1|awk -F: '{print $1}'` == "run" ];then
#       echo "1"
#    else
#       echo "0"
#    fi
#done

Process_num=$(ps -ef|grep runsv|grep $1|grep -v grep|wc -l)
if [ $Process_num -eq 1 ];then
    echo $Process_num
else
    echo 0
fi 
