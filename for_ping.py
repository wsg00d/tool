import time
import os

start_time = time.time()

for i in range(1,254):
    ip='192.168.2.'+str(i)
    a=os.popen('ping -n 2 '+ip).read()
    #print a
    if 'TTL' in a:
        print '%s is UP'%ip

end_time = time.time()
result = end_time - start_time
print 'the resutl time is: ', result
