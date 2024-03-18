data = []
# 从文件中读取爬好的数据
with open('origin_data.txt','r',encoding='utf8') as f:
    for i in f.readlines():
        data.append(i.replace('\n','').split(','))
dataf = []
# 筛选出符合课程要求的数据，通过if判断
for i in data:
    if i[1] == '工程师' and (i[2] == '门巴'):
        if i[5] == '未婚' and (i[6] == '高中'):
            if 1.96 >= float(i[4]) >= 1.69:
                dataf.append(i)
# 写入新文件中
with open('dxjsj-id-grp2022_042.txt','w',encoding='utf8') as f:
    for i in dataf:
        f.write('，'.join([i[3],i[4],i[6],i[5],i[2],i[1],i[7]])+'\n')