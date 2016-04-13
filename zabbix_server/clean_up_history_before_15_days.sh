#!/bin/bash

User="zbx_user"
Passwd="nidemima"
Date=`date -d $(date -d "-15 day" +%Y%m%d) +%s` #取15天之前的时间戳

$(which mysql) -u${User} -p${Passwd} -e "
use zabbix;
DELETE FROM history WHERE 'clock' < $Date;
optimize table history;
DELETE FROM history_str WHERE 'clock' < $Date;
optimize table history_str;
DELETE FROM history_uint WHERE 'clock' < $Date;
optimize table history_uint;
"

#      If you wanna clean up trends and events too
#      more information from zabbix offical web or http://www.furion.info/623.html

# DELETE FROM  trends WHERE 'clock' < $Date;
# optimize table  trends;
# DELETE FROM trends_uint WHERE 'clock' < $Date;
# optimize table trends_uint;
# DELETE FROM events WHERE 'clock' < $Date;
# optimize table events;