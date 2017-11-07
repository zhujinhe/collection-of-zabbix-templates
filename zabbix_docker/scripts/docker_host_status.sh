#!/bin/bash
#
docker_name=`sudo /usr/bin/docker ps -a|grep -v "CONTAINER ID"|awk '{print $NF}'`
for i in ${docker_name};do
   sudo /usr/bin/docker stats $i --no-stream |awk 'NR==2{a=$1;b=$2;c=$3$4;d=$6$7;e=$9$10;f=$12$13;g=$14$15;h=$17$18;j=$8}END{print "CONTAINER "a"\n""CPU "b"\n""MEMUSAGE "c"\n""LIMIT "d"\n""NETI-0 "e"\n""NETI-1 "f"\n""BLOCKI-0 "g"\n""BLOCKI-1 "h" \n""MEM "j}' |awk -F'%' '{print $1}' |awk '{a=/GiB/?$2*1024*1024*1024:(/M[i]?B/?$2*1024*1024:(/[Kk][Bb]/?$2*1024:(/B\>/?$2*1:$2)))}{print $1,a}' > /etc/zabbix/scripts/
