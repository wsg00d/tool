import requests
import json
def login():
    url_login='https://api.zoomeye.org/user/login'
    data={
    "username":"184180352@qq.com",
    "password":"wsisg00d!"
    }
    data=json.dumps(data)
    #print data
    r=requests.post(url=url_login,data=data)
    # #print r.status_code
    print json.loads(r.content)['access_token']
    return json.loads(r.content)['access_token']
def main():
    url='https://api.zoomeye.org/web/search?query=country:cn%20app:struts2&page=1&facets=app,os'
    headers={'Authorizatsion':'JWT '+login()}
    r=requests.get(url=url,headers=headers)
    datas=json.loads(r.content)['matches']
    for data in datas:
        biu= data['site']
        print biu
if __name__ == '__main__':
    main()