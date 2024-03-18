import pandas as pd
import csv
department = ['计',]
df = pd.read_excel('读者信息.xlsx')
data = []
for i in df.columns.values:
    data.append(df[i].tolist())
data1 = []
for i in range(len(data[0])):
    try:
        if data[3][i][:1] in department or data[3][i] == '计算机与科学技术学院':
            data1.append([data[0][i],data[1][i],data[2][i],data[3][i]])
    except:
        continue
data2 = []
for i in data1:
    if i not in data2:
        data2.append(i)
with open('读者信息清洗后.csv','w',newline='',encoding='utf-8') as f:
    fcsv = csv.writer(f)
    for i in data2:
        fcsv.writerow(i)