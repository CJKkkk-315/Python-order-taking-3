import csv
import pandas as pd
sid = []
with open('读者信息清洗后.csv','r') as f:
    fcsv = csv.reader(f)
    for i in fcsv:
        sid.append(i[0])
for year in ['2014','2015','2016','2017']:
    df = pd.read_excel(f'图书借还{year}.xlsx')
    df = df[df['读者ID'].isin(sid)]
    df = df.drop_duplicates(keep = 'first')
    df.to_excel(year+'.xlsx',index=False)