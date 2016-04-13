README.txt
方法1:
可以通过添加zabbix模块:
https://github.com/smoeding/zabbix-sendmail

方法2:
通过直接读取sendmail的文件来分析

sudo chmod +r /var/log/mail/statistics

示例
$ which mailstats
/usr/sbin/mailstats

MTA statistics...
Statistics from Wed Jul 22 20:02:04 2015
 M   msgsfr  bytes_from   msgsto    bytes_to  msgsrej msgsdis msgsqur  Mailer
 3       15        145K        0          0K        0       0       0  smtp
 4     1071      61483K      137      11664K     1681       0       0  esmtp
 7        0          0K       21        292K        0       0       0  relay
 8      907      14463K     1867      66122K       97       0       0  local
=====================================================================
 T     1993      76091K     2025      78078K     1778       0       0
 C    35374                 2044                15610
 
$ sudo mailstats  -P
1376404953 1458896928
 9        5          5        5          5        0       0       0  local
 T        5          5        5          5        0       0       0
 C        2        0      0

mailstats  -P| awk '/^ *T/ {
  received = received + $5
  sent = sent + $3
}

END {
  print "received.value", received
  print "sent.value", sent
}'