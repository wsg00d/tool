import requests
from bs4 import BeautifulSoup
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'}
url='https://bbs.ichunqiu.com/portal.php'
r=requests.get(url=url,headers=headers)
#print r.content
soup=BeautifulSoup(r.content,"html.parser")
print soup.title
print soup.title.string

bbs_news=soup.find_all(name='a',attrs={'class':'ui_colorG'})
for bbs in bbs_news:
    print bbs.string
