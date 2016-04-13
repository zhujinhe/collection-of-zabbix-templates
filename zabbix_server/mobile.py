#!/bin/env python
# -*- coding: utf8 -*-

import sys
import re
import requests
import time

#sms_api_addr = 'https://www.baidu.com/'
sms_api_addr = 'http://m.5c.com.cn/api/send/index.php'
username = 'nidezhanghao'
password = 'nidemima'
apikey = 'nidekay'
encode = 'utf-8'

if len(sys.argv) < 2:
    print("args less than 2")
    sys.exit(1)

content = sys.argv[2]
matchObj = re.match(r'^1\d{10}$', sys.argv[1], re.M | re.I)
if matchObj:
    mobile = matchObj.group()
    print(mobile)
else:
    print("Mobile format invalid")
    sys.exit(1)

def generate_md5(plaintext):
    import hashlib
    m = hashlib.md5()
    m.update(plaintext)
    return m.hexdigest()
password_md5 = generate_md5(password)


payload = {'username': username, 'password_md5': password_md5,
           'apikey': apikey, 'mobile': mobile,
           'content': content, 'encode': encode}

r = requests.get(sms_api_addr, params=payload)

print("URL", r.url)
request_log = "" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\r" + r.url + "\r" + r.text


with open('/var/log/zabbix/zabbix_alert.log', 'a') as f:
    f.write(request_log)

