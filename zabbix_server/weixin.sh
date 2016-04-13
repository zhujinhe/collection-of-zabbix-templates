#!/bin/bash
###SCRIPT_NAME:weixin.sh###
###send message from weixin for zabbix monitor###
###V1-2016-03-21###
CropID='nideid'
Secret='nidesecurity'
GURL="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=$CropID&corpsecret=$Secret" 
Gtoken=$(/usr/bin/curl -s -G $GURL | awk -F\" '{print $4}')
PURL="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=$Gtoken"
Content=$2
#/usr/bin/curl --data-ascii '{ "touser": "@all", "toparty": " @all ","msgtype": "text","agentid": "1","text": {"content": "'${Content}'"},"safe":"0"}' $PURL

UserID="$1"
Content="`echo $@|cut -d" " -f2-`"
AppID="1"
PartyID="2"

function weixin_body() {
        printf '{\n'
        printf '\t"touser": "%s",\n' $UserID
#        printf '\t"toparty": "%d",\n' $PartyID
        printf '\t"msgtype": "%s",\n' 'text'
        printf '\t"agentid": "%d",\n' $AppID
        printf '\t"text": {\n'
        printf "\t\t\"content\": \"${Content}\"\n"
        printf '},\n'
        printf ' "safe":"%d"\n' 0
        printf '}'
}
message=`weixin_body`
#message='{ "touser": "@all", "toparty": " @all ","msgtype": "text","agentid": "1","text": {"content": "'${Content}'"},"safe":"0"}'
#echo $message
/usr/bin/curl --data-ascii "$message" $PURL  |tee -a weixin.log
