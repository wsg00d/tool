# -*- coding: UTF-8 -*-
#author:wsg00d

from threading import Thread
import time
import os

def threadhandle(ip):
    a=os.popen('ping -n 2 '+ip).read()
    #print a
    if 'TTL' in a:
        print '%s is UP'%ip

if __name__ == '__main__':
    start_time = time.time()
    for i in range(1,255):
        ip='192.168.100.'+str(i)
        #print ip
        t = Thread(target=threadhandle, args=(ip,))
        #time.sleep(0.01)
        t.start()
    end_time=time.time()
    result=end_time-start_time
    print 'the resutl time is: ',result
