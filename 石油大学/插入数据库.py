# 数据表结构
# 除了必须的字段，其余根据自己的数据情况来决定插入哪个字段
# 自己的表一定要先备份好，误操作后便于自己恢复，别依赖他人
# 代码和数据文件也要经常备份！！！

'''
字段名次，数据类型，中文含义，处理方式
idst，整数，自动增加的内部号，不用管
stdid，字符串，学号，必须用
idcard，字符串，身份证号，必须用
name，字符串，姓名，看情况
height，浮点数，身高（单位m），看情况
weight，整数，体重（单位Kg），看情况
major，字符串，专业，看情况
education，字符串，学历，看情况
marriage，字符串，婚姻状况，看情况
nationality，字符串，民族（不含族），看情况
political_affiliation，字符串，政治面貌，看情况
professional_title，字符串，职称，看情况
registered_permanent_residence，字符串，户口性质，看情况
province，字符串，省，不用管
city，字符串，市，不用管
county，字符串，县（区），不用管
date_of_birth，日期，出生日期，不用管
gender，字符串，性别，不用管
checked，字符串，身份证是否合格，不用管
intime，日期时间，保存时间，可选
'''

import pymysql
import datetime

TableName = "kcbg_2022_2102030124"
UserId = "kcbg_2102030124"
Pswd = "ukga9W25"
try:
    # \ 代表主动折行
    cnct = pymysql.connect(host='172.19.163.200', user=UserId, password=Pswd, \
      port=3306, db='dxjsjkcbg', charset='utf8')
except:
    print("connect error")
    exit()
crsr = cnct.cursor()
sSql = "SELECT * FROM " + TableName + " WHERE stdid=%s"
rs = []
with open('dxjsj-id-grp2022_042.txt','r',encoding='utf8') as f:
    for i in f.readlines():
        if i.replace('\n','').split('，') not in rs:
            rs.append(i.replace('\n','').split('，'))
print(rs)
for r in rs:
    Sql0 = "INSERT INTO " + TableName + \
      " (stdid, professional_title, nationality, idcard, height, marriage,education,registered_permanent_residence) VALUES"
    professional_title = r[5]
    nationality = r[4]
    idcard = r[0]
    height = r[1]
    marriage = r[3]
    education = r[2]
    registered_permanent_residence = r[6]
    Values = (UserId, professional_title, nationality, idcard, height, marriage,education,registered_permanent_residence)
    print(len(Values))
    sSql = Sql0 + str(Values)
    print(sSql)
    i = crsr.execute(sSql)
    cnct.commit()
    print('inserted')
crsr.close()
cnct.close()