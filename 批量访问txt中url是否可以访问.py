import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}

with open('idno.txt','r') as f:
    for line in f:
        line=line.strip('\n')
        url1='http://'+line
        url2='https://'+line

        try:
            r1=requests.get(url=url1,timeout=5)
            if r1.status_code==200:
                print url1
                file='bicointime.txt'
                with open(file,'a+') as g:
                    g.write(url1+'\n')
                    g.close()
        except:
            pass
        try:
            r2=requests.get(url=url2,verify=False,timeout=5)
            if r1.status_code==200:
                print url2
                file = 'bicointime1.txt'
                with open(file, 'a+') as g:
                    g.write(url2+'\n')
                    g.close()
        except:
            pass
