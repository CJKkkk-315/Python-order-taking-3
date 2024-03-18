with open('data.txt','r',encoding='utf8') as f:
    data = [i.replace('\n','').split(',') for i in f.readlines()]
res = []
for i in data:
    if float(i[5]) > 2.00 or float(i[5]) < 1.59:
        if i[4] == '专科' or i[4] == '本科':
            if 118 > float(i[2]) > 50:
                if i[3] == '民盟盟员' and i[1][0] in ['薛','申']:
                    res.append(i)
with open('dxjsj-id-grp2022_015.txt','w',encoding='utf8') as f:
    for i in res:
        f.write('，'.join(i) + '\n')