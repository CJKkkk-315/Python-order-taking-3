import csv
import pandas as pd
df = pd.read_excel('图书目录.xlsx')
with open('《中国图书馆图书分类法》简表.txt','r',encoding='utf-8') as f:
    data = f.readlines()
data = [i.replace('\n','').replace('\u3000','').replace(' ','') for i in data if i and i[0] != '-']
df = df.values.tolist()
res = []
for i in df:
    try:
        c = i[2].split('/')[0]
    except:
        continue
    for j in data:
        if c == j[:len(c)]:
            cate = j[len(c):]
            # print(i[:2]+[cate])
            res.append(i[:2]+[cate])
            break
with open('图书目录清洗后.csv','w',encoding='utf-8',newline='') as f:
    fcsv = csv.writer(f)
    for i in res:
        fcsv.writerow(i)