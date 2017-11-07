#!//usr/bin/python
"""
get value 
meikong zhenghe, jiandan xiexie
"""
import sys
import requests
url = 'http://10.46.224.57:15672/api/queues/%2F' + sys.argv[1][1:] + '/' + sys.argv[2]
ret = requests.get(url=url, auth=('guest', 'guest'))
print ret.json()[sys.argv[3]]

