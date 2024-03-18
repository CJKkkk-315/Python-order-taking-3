with open('data1.txt','r',encoding='utf8') as f:
    data1 = [i.replace('\n','').split(',') for i in f.readlines()]
with open('data2.txt','r',encoding='utf8') as f:
    data2 = [i.replace('\n','').split(',') for i in f.readlines()]
data = []
for i in data1:
    data.append([i[6],i[3],i[9],i[4],'',i[8],i[7]])
for i in data2:
    data.append([i[1],i[3],i[5],i[9],i[8],i[4],i[2]])
with open('data.txt','w',encoding='utf8') as f:
    for i in data:
        f.write('，'.join(i) + '\n')
with open('data.txt','r',encoding='utf8') as f:
    data = [i.replace('\n','').split('，') for i in f.readlines()]
res = []
for i in data:
    if float(i[2]) > 2.00 or float(i[2]) < 1.59:
        if i[5] == '专科' or i[5] == '本科':
            if 118 > float(i[3]) > 50:
                if i[6] == '民盟盟员' and i[1][0] in ['薛','申']:
                    res.append(i)
with open('dxjsj-id-grp2022_015.txt','w',encoding='utf8') as f:
    for i in res:
        f.write('，'.join(i) + '\n')
import pymysql
TableName = "kcbg_2022_2104010203"
UserId = "kcbg_2104010203"
Pswd = "7RTuCFfH"
cnct = pymysql.connect(host='172.19.163.200', user=UserId, password=Pswd, \
      port=3306, db='dxjsjkcbg', charset='utf8')
crsr = cnct.cursor()
for row in res:
    Sql0 = "INSERT INTO " + TableName + \
           " (stdid, idcard, name. height, weight,major, education,political_affiliation) VALUES"
    professional_title = row[0]
    name = row[1]
    weight = row[2]
    political_affiliation = row[3]
    education = row[4]
    height = row[5]
    registered_permanent_residence = row[6]
    Values = (
    UserId, professional_title, name, weight, political_affiliation, education, height, registered_permanent_residence)
    sSql = Sql0 + str(Values)
    i = crsr.execute(sSql)
    cnct.commit()
    print('inserted')
crsr.close()
cnct.close()