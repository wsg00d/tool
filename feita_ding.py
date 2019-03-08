#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import time

f=open('idno.txt','r')
incidentserialno1 = f.read()
f.close()

DING_URL = "https://oapi.dingtalk.com/robot/send?access_token=a84e9a7396b8a8dbfd69c7463511d25dfea9f969a18bb4845af8c894a091ab4e"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
data = {'ajax': 1, 'username': 'wangsong', 'secretkey': 'gRvsU99bQgcMmcmX'}
url1 = 'https://10.161.1.254/logincheck'
url2='https://10.161.1.254/p/logs/ips/json/?filter=%5B%5D&serial_no=FGT5HD3917800776'
url3='https://10.161.1.254/logout'

session = requests.Session()
r1 = session.post(url=url1, data=data, headers=headers, verify=False)
r2=session.get(url=url2,headers=headers,verify=False)

print len(r2.content)
if len(r2.content)>5000:
    a=json.loads(r2.content)
else:
    session = requests.Session()
    r1 = session.post(url=url1, data=data, headers=headers, verify=False)
    r2 = session.get(url=url2, headers=headers, verify=False)
    print r2.content
    a = json.loads(r2.content)
    print a
nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

f = open('test1.txt', 'w')
f.write(nowtime + "\n" + str(len(r2.content))+"\n")
f.close()

if 'user' not in a['source'][0]:
    content = nowtime + "\nattack: " + a['source'][0]['attack'] + "\nlevel: " + a['source'][0][
        'crlevel'] + "\ndirection: " + a['source'][0]['direction'] + "\nsrcip: " + a['source'][0][
                  'srcip'] + "\ndstip: " + a['source'][0]['dstip'] + "\nhostname: " + a['source'][0]['hostname']
#print content


incidentserialno2 = a['source'][0]['incidentserialno']
if incidentserialno1 != incidentserialno2:

    f=open('idno.txt','w')
    f.write(incidentserialno2)
    f.close()


    if 'user' not in a['source'][0]:
        content= nowtime + "\nattack: " + a['source'][0]['attack'] + "\nlevel: " + a['source'][0]['crlevel']  + "\ndirection: " + a['source'][0]['direction'] + "\nsrcip: " + a['source'][0]['srcip'] + "\ndstip: " + a['source'][0]['dstip'] + "\nhostname: " + a['source'][0]['hostname']

    else:
        if 'hostname' not in a['source'][0]:
            content = nowtime + "\n" + a['source'][0]['msg'] + "\nlevel: " + a['source'][0]['crlevel'] + "\nuser: " + a['source'][0]['user'] + "\ndirection: " + a['source'][0]['direction'] + "\nsrcip: " + a['source'][0]['srcip'] + "\ndstip: " + a['source'][0]['dstip'] + "\nhostname: " + a['source'][0]['dstintf']
        else:
            content = nowtime + "\nattack: " + a['source'][0]['attack'] + "\nlevel: " + a['source'][0]['crlevel'] + "\nuser: " + a['source'][0]['user'] + "\ndirection: " + a['source'][0]['direction'] + "\nsrcip: " + a['source'][0]['srcip'] + "\ndstip: " + a['source'][0]['dstip'] + "\nhostname: " + a['source'][0]['hostname']

    print content
    data = {
            "msgtype": "text",
            "text": {
                "content": content
            },
            "at": {
                "isAtAll": False
            }
        }

    header = {
            "Content-Type": "application/json",
            "charset": "utf-8"
    }
    sendData = json.dumps(data)
    print sendData

    incidentserialno1 = incidentserialno2
    request = requests.post(url=DING_URL, data=sendData, headers=header)
    print request.content

else:
    print nowtime

r3=session.get(url=url3,headers=headers,verify=False)
