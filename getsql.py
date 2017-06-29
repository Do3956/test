#coding:utf8

num_userid = {}
with open('fff.txt', "rb") as f:
    for line in f.readlines():
        userid, num = map(int, line.split(","))
        if num_userid.has_key(num):
            num_userid[num].append(userid)
        else:
            num_userid[num] = [userid]

sum = 0

sql = "insert into  [bsfb_DB0530].[dbo].[email_info] (title,content,type,time,toUserType,awardInfo,userContent) values " \
      "('手气卡异常补发','5月4日10点至5月12日17点使用手气卡补发',1,getdate(),2,'2,%s','%s')"
for num, useridlist in num_userid.items():
    listnum = len(useridlist)
    # print sql % (num, useridlist[:200])
    sum += 199
    if listnum>=200:
        for i in range(200, listnum,200):
            # if i+200
            sum += 199
            # print sql % (num, useridlist[i:i+200])