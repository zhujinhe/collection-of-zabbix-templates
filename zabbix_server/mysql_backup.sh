#!/bin/bash
# Program
# mysql_daliy_backup
# Author:zhujh2
# 20140820

PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

WD=/root/backup

[ ! -d $WD ] && mkdir -p $WD 

MysqlPass=`cat $WD/Mysql.pass`
BackupDate=`date +%Y%m%d%H%M`

echo backup process starts at $BackupDate >> $WD/backup.log ;
/usr/local/mysql-5.6/bin/mysqldump -uroot -p$MysqlPass --master-data --single-transaction --all-databases > $WD/$BackupDate.sql ;
#old
#/usr/local/mysql-5.6/bin/mysqldump -uroot -p$MysqlPass --opt -R --events --ignore-table=mysql.events --all-databases > $WD/$BackupDate.sql ;
echo backup process ends at  `date +%Y%m%d%H%M`  >> $WD/backup.log ;

find $WD -name "*.sql" -mtime +45 -exec rm -rf  {} \; 
