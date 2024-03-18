import sqlite3
import csv
import math
conn = sqlite3.connect('book.db')
print ("数据库打开成功")
c = conn.cursor()
c.execute("DROP TABLE BOOK;")
conn.commit()
c.execute('''CREATE TABLE BOOK
       (
       NAME           CHAR(50)    ,
       CATE            CHAR(50)     ,
       SUBCATE        CHAR(50),
       WRITER        CHAR(50),
       PRICE          FLOAT,
       TIME          CHAR(50),
       COMPANY       CHAR(50),
       SCORE         FLOAT,
       PEOPLE         INT ,
       CONTENT        TEXT);''')
print ("数据表创建成功")
conn.commit()
data = [i for i in csv.reader(open('res.csv', 'r', encoding='utf8'))]
dataf = []
for i in range(len(data)):
    try:
        s = data[i][4]
        aw = ''
        for j in s:
            if j.isdigit() or j == '.':
                aw += j
        if float(aw) > 150:
            continue
        data[i][4] = float(aw)
        data[i][7] = float(data[i][7])
        data[i][8] = math.log(int(data[i][8].replace('(','').replace(')','').replace('人评价','')),10)
        dataf.append(data[i])
    except:
        continue
print(len(data))
print(len(dataf))
for i in dataf:
    try:
        c.execute(f"INSERT INTO BOOK (NAME,CATE,SUBCATE,WRITER,PRICE,TIME,COMPANY,SCORE,PEOPLE,CONTENT)\
              VALUES ('{i[0]}','{i[1]}','{i[2]}','{i[3]}',{i[4]},'{i[5]}','{i[6]}',{i[7]},{i[8]},'{i[9]}' )")
    except:
        print(i)
conn.commit()
print("数据插入成功")
conn.close()
