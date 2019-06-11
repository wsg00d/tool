#!/usr/bin/env python
#coding=utf-8

import re
import sys
import json
import time
import mysql.connector
from aliyunsdkcore.client import AcsClient
from aliyunsdkram.request.v20150501.ListPoliciesForUserRequest import ListPoliciesForUserRequest
from aliyunsdkram.request.v20150501.ListGroupsRequest import ListGroupsRequest
from aliyunsdkram.request.v20150501.ListUsersForGroupRequest import ListUsersForGroupRequest
from aliyunsdkram.request.v20150501.ListPoliciesForGroupRequest import ListPoliciesForGroupRequest
from aliyunsdkram.request.v20150501.ListUsersRequest import ListUsersRequest

reload(sys)
sys.setdefaultencoding('utf-8')
client = AcsClient('LT*******Z1', 'NC8***************Ra', 'cn-hangzhou')    #aliyun accesskey
hostname = '10.1.1.3'      # 数据库主机地址
username = 'root'          # 数据库用户名
password = '123456'        # 数据库密码
databases = 'otc_security'  # 数据库名


##ListUsersRequest列出所有用户##
def LUR():
    request_ListUsersRequest= ListUsersRequest()
    request_ListUsersRequest.set_accept_format('json')
    response_ListUsersRequest = client.do_action_with_exception(request_ListUsersRequest)
    r_ListUsersRequest=re.compile(r'UserName":"([0-9a-z_A-Z_]*)","UpdateDate"')
    r_ListUsersRequest_array=r_ListUsersRequest.findall(response_ListUsersRequest)
    return r_ListUsersRequest_array


##ListPoliciesForUserRequest列出特定用户权限##
def  LPFUR(username):
    request_ListPoliciesForUserRequest = ListPoliciesForUserRequest()
    request_ListPoliciesForUserRequest.set_accept_format('json')
    request_ListPoliciesForUserRequest.set_UserName(username)
    response_ListPoliciesForUserRequest = client.do_action_with_exception(request_ListPoliciesForUserRequest)
    return response_ListPoliciesForUserRequest


##ListUsersForGroupRequest列出用户组中的所有用户##
def LUFGR(groupname):
    request_ListUsersForGroupRequest= ListUsersForGroupRequest()
    request_ListUsersForGroupRequest.set_accept_format('json')
    request_ListUsersForGroupRequest.set_GroupName(groupname)
    response_ListUsersForGroupRequest= client.do_action_with_exception(request_ListUsersForGroupRequest)
    return response_ListUsersForGroupRequest


##ListGroupsRequest列出所有组##
def LGR():
    request_ListGroupsRequest= ListGroupsRequest()
    request_ListGroupsRequest.set_accept_format('json')
    response_ListGroupsRequest= client.do_action_with_exception(request_ListGroupsRequest)
    r_ListGroupsRequest=re.compile(r'GroupName":"([0-9a-z_A-Z_]*)","UpdateDate"')
    r_ListGroupsRequest_array=r_ListGroupsRequest.findall(response_ListGroupsRequest)
    return r_ListGroupsRequest_array


##ListPoliciesForGroupRequest列出用户组权限##
def LPFGR(groupname):
    request_ListPoliciesForGroupRequest= ListPoliciesForGroupRequest()
    request_ListPoliciesForGroupRequest.set_accept_format('json')
    request_ListPoliciesForGroupRequest.set_GroupName(groupname)
    response_ListPoliciesForGroupRequest = client.do_action_with_exception(request_ListPoliciesForGroupRequest)
    return response_ListPoliciesForGroupRequest


##写入数据库##
def datainsert(username,privilege,remark,creattime,inserttime,id,hostname1=hostname,username1=username,password1=password,databases1=databases):
    mydb = mysql.connector.connect(
        host=hostname1,
        user=username1,
        passwd=password1,
        database=databases1
    )
    mycursor = mydb.cursor()
    sql1 = "INSERT INTO otc_database (负责人,业务,账号,数据库权限,描述,赋权时间,数据同步时间) VALUES (%s, %s,%s,%s,%s,%s,%s)"
    val = ('王**', 'otc', username, privilege, remark,creattime, inserttime)
    sql2 = "INSERT INTO otc_server (负责人,业务,账号,服务器权限,描述,赋权时间,数据同步时间) VALUES (%s, %s,%s,%s,%s,%s,%s)"
    val = ('王**', 'otc', username, privilege, remark, creattime, inserttime)
    if id==1:
        sql=sql1
    else:
        sql=sql2
    mycursor.execute(sql, val)
    mydb.commit()  # 数据表内容有更新，必须使用到该语句
    print(mycursor.rowcount, "data insert success!")


##数据库去重当天同步用户组和用户个人重复的权限,不去重之前的数据##
def datasplit(hostname1=hostname,username1=username,password1=password,databases1=databases):
    mydb = mysql.connector.connect(
        host=hostname1,
        user=username1,
        passwd=password1,
        database=databases1
    )
    mycursor = mydb.cursor()
    sql="delete from otc_database where (账号,数据库权限) in (select 账号,数据库权限 from (select 账号,数据库权限 from \
    otc_database group by 账号,数据库权限 having count(数据库权限)>1 ) as tmp1) and 数据同步时间 >= (now()-interval 5 hour) \
    and 数据同步时间<= now() and id not in (select id from (select min(id) id from otc_database group by 账号,数据库权限 having count(账号)>1) as tmp2);"
    mycursor.execute(sql)
    mydb.commit()


##main##
if __name__ == '__main__':

    r_ListUsersRequest_array=LUR()
    for i in range(0,len(r_ListUsersRequest_array)):
        LPFUR(r_ListUsersRequest_array[i])
        quanxian=json.loads(LPFUR(r_ListUsersRequest_array[i]))
        for j in range(0,len(quanxian['Policies']['Policy'])):
            list = []
            list.append(r_ListUsersRequest_array[i])
            list.append(quanxian['Policies']['Policy'][j]['PolicyName'])
            list.append(quanxian['Policies']['Policy'][j]['Description'])
            b=quanxian['Policies']['Policy'][j]['AttachDate'].replace('T',' ')
            b = b.replace('Z', ' ')
            list.append(b)
            nowtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            match_obj2=str(list[2])
            if '数据库' in match_obj2:
                id=1
                datainsert(list[0],list[1],list[2],list[3],nowtime,id)
            if '服务器' in match_obj2:
                id=2
                datainsert(list[0], list[1], list[2], list[3], nowtime,id)
            if '管理所有阿里云资源的权限' in match_obj2:
                id = 1
                datainsert(list[0], list[1], list[2], list[3], nowtime, id)
                id = 2
                datainsert(list[0], list[1], list[2], list[3], nowtime, id)



    r_ListGroupsRequest_array=LGR()
    for k in range(0,len(r_ListGroupsRequest_array)):
        employee=json.loads(LUFGR(r_ListGroupsRequest_array[k]))
        for x in range(0,len(employee['Users']['User'])):
            list1=[]
            list1.append(employee['Users']['User'][x]['UserName'])
            r_ListPoliciesForGroupRequest_array = json.loads(LPFGR(r_ListGroupsRequest_array[k]))
            for l in range(0,len(r_ListPoliciesForGroupRequest_array['Policies']['Policy'])):
                match_obj1 = str(r_ListPoliciesForGroupRequest_array['Policies']['Policy'][l]['Description'])
                list1.append(r_ListPoliciesForGroupRequest_array['Policies']['Policy'][l]['PolicyName'])
                list1.append(r_ListPoliciesForGroupRequest_array['Policies']['Policy'][l]['Description'])
                b = r_ListPoliciesForGroupRequest_array['Policies']['Policy'][l]['AttachDate'].replace('T', ' ')
                b = b.replace('Z', ' ')
                list1.append(b)
                if '数据库' in match_obj1:
                    id=1
                    datainsert(list1[0],list1[1],list1[2],list[3],nowtime,id)
                    del list1[1]
                    del list1[1]
                    del list1[1]
                if '服务器' in match_obj1:
                    id=2
                    datainsert(list1[0], list1[1], list1[2], list[3], nowtime,id)
                    del list1[1]
                    del list1[1]
                    del list1[1]
                if '管理所有阿里云资源的权限' in match_obj1:
                    id = 1
                    datainsert(list[0], list[1], list[2], list[3], nowtime, id)
                    del list1[1]
                    del list1[1]
                    del list1[1]
                    id = 2
                    datainsert(list[0], list[1], list[2], list[3], nowtime, id)
                    del list1[1]
                    del list1[1]
                    del list1[1]
    datasplit()
