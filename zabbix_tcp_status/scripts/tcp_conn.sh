#!/bin/bash
#tcp status
#
metric=$1

case $metric in
   closed)
          output=$(ss -s|grep "TCP"|grep estab|awk '{print $6}'|awk -F, '{print $1}')
          if [ "$output" == "" ];then
             echo 0
          else
             echo $output
          fi
        ;;
   estab)
          output=$(ss -s|grep "TCP"|grep estab|awk '{print $4}'|awk -F, '{print $1}')
          if [ "$output" == "" ];then
             echo 0
          else
             echo $output
          fi
        ;;
   timewait)
          output=$(ss -s|grep "TCP"|grep estab|awk '{print $12}'|awk -F/ '{print $1}')
          if [ "$output" == "" ];then
             echo 0
          else
             echo $output
          fi
        ;;
   orphaned)
          output=$(ss -s|grep "TCP"|grep estab|awk '{print $8}'|awk -F, '{print $1}')
          if [ "$output" == "" ];then
             echo 0
          else
             echo $output
          fi
        ;;
         *)
          echo -e "\e[033mUsage: sh  $0 [closed|estab|timewait|orphaned]\e[0m"
esac
