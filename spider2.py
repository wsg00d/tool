import requests
import re
import os
import sys
from selenium import webdriver
reload(sys)
sys.setdefaultencoding('utf8')
cookies={
'ci_session':'c9422c4dbef501ef4ad310c6ac4944bfacd4ccd4'
}
for i1 in range(1,3):
    url = 'http://192.168.1.254/index.php/Education/edubook?uname=&per_page=' + str(i1)
    html1= requests.get(url=url, cookies=cookies)
    b1 = re.findall('<a title=".*" href="(http://192\.168\.1.254/index\.php/Education/bookdetail\?packageid=.*)">',
                   html1.content)
    for i2 in b1:
        html2=requests.get(url=i2,cookies=cookies)
        title=str(re.findall('<div class="courseName" title="(.*)">',html2.content)[0]).encode('gb18030').decode('gbk')
        print title
        os.makedirs('C:\\Users\\yxzc\\Desktop\\awd\\shiyan1\\'+title)
        b2=re.findall('<a href="(http://192\.168\.1\.254/index\.php/Education/sectiondetail\?packageid=[0-9]*&sectionid=[0-9]*)">',html2.content)
        for i3 in b2:
            brower = webdriver.PhantomJS()
            brower.get(i3)
            brower.delete_all_cookies()
            cookie = {
                'domain': '192.168.1.254',
                'name': 'ci_session',
                'value': '03d0b33f8b0809b4ca50323899d838e0538a6644',
                'path': '/',
                'expires': None
            }
            brower.add_cookie(cookie)
            brower.get(i3)
            picName = re.findall('<span class="secName">(.*)</span>', brower.page_source.encode('gb18030'))[0].decode(
                'gbk')
            brower.maximize_window()
            path='C:\\Users\\yxzc\\Desktop\\awd\\shiyan1\\'+title+ '\\'+picName + '.png'
            print path
            brower.save_screenshot('C:\\Users\\yxzc\\Desktop\\awd\\shiyan1\\'+title+ '\\'+picName + '.png')
            brower.close()
