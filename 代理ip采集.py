# coding=utf-8

import requests
from bs4 import BeautifulSoup as bs
import re

def proxycheck(ip,port,types):
    proxy={}
    proxy[types.lower()] = ip + ':' + port
    headers={'token':'fa0f3448c16ca5accf9e71c1b838bd43'}
    url='http://api.ip138.com/query/?'
    try:
        r=requests.get(url=url,headers=headers,proxies=proxy,timeout=4)
        print r.content
    except:
        print 'error'

headers1={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

url1='http://www.xicidaili.com/nn/'


r=requests.get(url=url1,headers=headers1)
soup=bs(r.content,"html.parser")
a=soup.find_all(name='tr',attrs={'class':re.compile('|[^odd]')})
for i in a:
    soup1=bs(str(i),"html.parser")
    b=soup1.find_all(name='td')
    print b[1].string,b[2].string,b[5].string

    proxycheck(b[1].string,b[2].string,b[5].string)






