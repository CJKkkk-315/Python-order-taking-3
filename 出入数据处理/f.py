import pandas as pd
import os
for d in ['2019.12.1-2020.11.30','2020.12.1-2021.11.30','2021.12.1-2022.06.01']:
    filelist = os.listdir(f'{d}')
    for file in filelist:
        data = pd.read_excel(f'{d}/{file}').values.tolist()
        res = []
        for i in data:
            if str(i[0]) == 'nan':
                continue
            if '打印' in i[0]:
                continue
            if '时间' in i[0]:
                continue
            res.append(i[0])
        ans = [[res[0],res[1]]]
        for i in range(2,len(res),2):
            if res[i] == ans[-1][0]:
                ans[-1].append(res[i+1])
            else:
                ans.append([res[i],res[i+1]])
        import csv
        with open(f'{d}/{file.replace("xls","")+"csv"}','w',newline='') as f:
            fcsv = csv.writer(f)
            for i in ans:
                fcsv.writerow(i)
        os.remove(f'{d}/{file}')