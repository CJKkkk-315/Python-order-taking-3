import pandas as pd
from itertools import combinations
money = 0
df = pd.read_excel('待开票清单3.xlsx')
data = df.values.tolist()
target = []
pf = []
for i,j in enumerate(data):
    if str(j[4]) != 'nan':
        target.append([i+2,*list(map(lambda x:round(x,2),j[4:8]))])
target = target[:-1]
use = []
for i,j in enumerate(data):
    if str(j[10]) != 'nan':
        use.append([i+2,*list(map(lambda x:round(x,2),j[10:14]))])
res1 = []
for i in target:
    for j in use:
        if i[1:] == j[1:]:
            res1.append([i,j])
for r in res1:
    targett = r[0]
    pf.append([targett[0],[r[1][0]],[r[1][0]]])
    money += targett[1]
for i in res1:
    target.remove(i[0])
    use.remove(i[1])
target.sort(key=lambda x:x[1],reverse=True)
# print(target)
zpuse = use[::]
ppuse = use[::]
rr = []

for targett in target:
    zpzh = []
    ppzh = []
    flag = 0
    for time in range(2,10):
        if flag:
            break
        # print(time)
        for i in list(combinations(zpuse,time)):
            if abs(sum([j[2] for j in i])-targett[2]) <= 0.03:
                if abs(sum([j[3] for j in i])-targett[3]) <= 0.03:
                    zpzh.append([t for t in i])
                    flag = 1
                    break
    flag = 0
    for time in range(2,10):
        if flag:
            break
        # print(time)
        for i in list(combinations(ppuse,time)):
            if abs(sum([j[2] for j in i])-targett[4]) <= 0.03:
                ppzh.append([t for t in i])
                flag = 1
                break
    try:
        for i in zpzh[0]:
            zpuse.remove(i)
        for i in ppzh[0]:
            ppuse.remove(i)
    except:
        continue
    pf.append([targett[0],[[j[0] for j in i] for i in zpzh][0],[[j[0] for j in i] for i in ppzh][0]])
    money += targett[1]
for i in pf:
    print(f'行数：{i[0]},专票金额与增值税金组合：{",".join(list(map(str,i[1])))},普票金额组合：{",".join(list(map(str,i[2])))}')
print(f'总计{round(money,2)}元')