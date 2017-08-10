import requests
headers={
'Host': '',
'Proxy-Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Referer': '',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.8',
'Cookie': '',
}
for i in range(8676,11035):
    url='http://xxx.xxxx.com:11111//DataManagement/MyDataView.aspx?TableId=1&DataAuthority=0&RecordId='+str(i)
    #print url
    r=requests.get(url=url,headers=headers)
    print r.status_code
    print i
    if(len(r.content)>10000):
        file='C:/Users/lenovo/Desktop/test/'+str(i)+'.html'
        f=open(file,'w')
        f.write(r.content)
        f.close