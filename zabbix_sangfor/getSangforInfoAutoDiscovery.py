#!/usr/bin/env python
# -*- coding: utf8 -*-
import sys
reload(sys)

sys.setdefaultencoding('utf8')

__author__ = 'zhujinhe'

import urllib2, json, re
from sharepoint import SharePointSite, basic_auth_opener
from ntlm import HTTPNtlmAuthHandler
from IPy import IP

server_url = 'http://so.nideyuming.com.cn/'
site_name = ''
ntlm_username = 'zhanghao'
ntlm_password = 'mima'
site_url = server_url + site_name


password_manager = urllib2.HTTPPasswordMgrWithDefaultRealm()
password_manager.add_password(None, server_url, ntlm_username, ntlm_password)
auth_handler = HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(password_manager)
opener = urllib2.build_opener(auth_handler)
site = SharePointSite(site_url, opener)


# # get lists of default site.
# for sp_list in site.lists:
#     print sp_list.id, sp_list.meta['Title']



lists_bj = site.lists['{136D0527-DC8C-454F-A369-A064310E3BE0}']

resdata = {}
resdata['data'] = []


VPN_STATUS = u'\u8425\u4e1a\u4e2d'
for row in lists_bj.rows:
    row_data = {}
    # {'{#VPN.TYPE}': 'WOC550', '{#VPN.ID}': 5,
    # '{#VPN.STATUS}': u'\u8425\u4e1a\u4e2d', '{#VPN.ADMIN}': u'\u79e6\u52c7',
    # '{#VPN.VPNID}': u'<div><font size=2 face="\u5b8b\u4f53">bj-0004-25</font></div>',
    # '{#VPN.GATEWAY}': '10.50.1.128/25', '{#VPN.STORENAME}': u'\u897f\u65af\u83b1\u5e97',
    # '{#VPN.Policy}': u'\u53cc\u7ebf\u8def\u7ec4'}
    if row._x8425__x4e1a__x72b6__x6001_ == VPN_STATUS:
    #    row_data['{#VPN.ID}'] = row.id
        row_data['{#VPN.VPNID}'] = str(re.findall(r'\w{2}-\d{4}-\d{2}', row.VPN_x0020_ID)[0])
    #    row_data['{#VPN.TYPE}'] = row._x8bbe__x5907__x578b__x53f7_
        row_data['{#VPN.GATEWAY}'] = str(IP(row.IP_x5730__x5740_)[1]).strip()
    #    row_data['{#VPN.POLICY}'] = row._x5355__x7ebf__x8def__x7ec4__x00
        row_data['{#VPN.STORENAME}'] = row._x5e97__x540d_.strip()
    #    row_data['{#VPN.STATUS}'] = row._x8425__x4e1a__x72b6__x6001_
        row_data['{#VPN.ADMIN}'] = row._x5b9e__x65bd__x5de5__x7a0b__x5e
        resdata['data'].append(row_data)
        # print(row.IP_x5730__x5740_)

# print(resdata)

#res = json.dumps(resdata,sort_keys=True, indent=4)
res = json.dumps(resdata,sort_keys=True,ensure_ascii=False)
print res
