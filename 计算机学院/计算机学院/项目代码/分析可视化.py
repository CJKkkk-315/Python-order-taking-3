import pandas as pd
import csv
from collections import Counter
from matplotlib.ticker import MaxNLocator
import matplotlib.pyplot as plt
# 将文件数据读入变量中，同时转为list类型
book = pd.read_csv('图书目录清洗后.csv',)
user = pd.read_csv('读者信息清洗后.csv',)
d2014 = pd.read_excel('2014.xlsx')
d2014 = d2014.values.tolist()
d2015 = pd.read_excel('2015.xlsx')
d2015 = d2015.values.tolist()
d2016 = pd.read_excel('2016.xlsx')
d2016 = d2016.values.tolist()
d2017 = pd.read_excel('2017.xlsx')
d2017 = d2017.values.tolist()
book = book.values.tolist()
user = user.values.tolist()
t = []
bookd = {}
tucate = []
tuxiaoshuo = []
ttucate = []
ttuxiaoshuo = []
# 定义书本编号和书本名及类别的键值对字典
for i in book:
    bookd[i[0]] = i[1:]
# 定义教师编号列表
for i in user:
    if i[1] == '教师':
        t.append(i[0])
def f1(data,year):
    tall = 0
    sall = 0
    tcates = []
    scates = []
    txiaoshuo = []
    sxiaoshuo = []
    tmeihuan = []
    smeihuan = []
    # 遍历所有数据
    for i in data:
        # 将老师与学生的数据分开存放
        if i[1] == '借' and i[3] in t:
            tall += 1
            try:
                # 将书本类型存放到tcates列表中
                tcates.append(bookd[i[2]][1])
                if '小说' in bookd[i[2]][1]:
                    # 若是小说，则存放到txiaoshuo列表中
                    txiaoshuo.append(bookd[i[2]][0])
            except:
                continue
        # 学生同理
        elif i[1] == '借' and i[3] not in t:
            sall += 1
            try:
                scates.append(bookd[i[2]][1])
                if '小说' in bookd[i[2]][1]:
                    sxiaoshuo.append(bookd[i[2]][0])
            except:
                continue
    # 再次遍历数据
    for i in range(len(data)):
        # 找出借了未还的数据
        if data[i][1] == '借':
            for j in range(i,len(data)):
                if data[j][1] == '还' and data[j][2:] == data[i][2:]:
                    break
            # 同样教师与学生分开存放
            if data[i][3] in t:
                if data[i][2] in bookd:
                    tmeihuan.append(bookd[data[i][2]][1])
            else:
                if data[i][2] in bookd:
                    smeihuan.append(bookd[data[i][2]][1])
    # 将上述处理好的数据排序后利用Counter函数统计输出
    print('{}年教师所借书籍类别前十为：'.format(year))
    s = ','.join([i[0] for i in sorted([[i,j] for i,j in Counter(tcates).items()],key=lambda x:x[1],reverse=True)[:10]])

    print(s)
    print('{}年学生所借书籍类别前十为：'.format(year))
    s = ','.join([i[0] for i in sorted([[i,j] for i,j in Counter(scates).items()],key=lambda x:x[1],reverse=True)[:10]])
    print(s)
    print('{}年教师所借小说前十为：'.format(year))
    s = ','.join([i[0] for i in sorted([[i,j] for i,j in Counter(txiaoshuo).items()],key=lambda x:x[1],reverse=True)[:10]])
    print(s)
    print('{}年学生所借小说前十为：'.format(year))
    s = ','.join([i[0] for i in sorted([[i,j] for i,j in Counter(sxiaoshuo).items()],key=lambda x:x[1],reverse=True)[:10]])
    print(s)
    print('{}年教师一共借了{}本书'.format(year,tall))
    print('{}年学生一共借了{}本书'.format(year,sall))
    print('{}年教师一共未归还{}本书'.format(year, len(tmeihuan)))
    print('{}年学生一共未归还{}本书'.format(year, len(smeihuan)))
    print('{}年教师未还类别前十为：'.format(year))
    s = ','.join([i[0] for i in sorted([[i, j] for i, j in Counter(tmeihuan).items()], key=lambda x: x[1], reverse=True)[:10]])
    print(s)
    print('{}年学生未还类别前十为：'.format(year))
    s = ','.join([i[0] for i in sorted([[i, j] for i, j in Counter(smeihuan).items()], key=lambda x: x[1], reverse=True)[:10]])
    print(s)
    # 同时将部分数据放入新列表中方便后续画图使用
    tucate.append([i[0] for i in sorted([[i, j] for i, j in Counter(scates).items()], key=lambda x: x[1], reverse=True)])
    tuxiaoshuo.append([i[0] for i in sorted([[i, j] for i, j in Counter(sxiaoshuo).items()], key=lambda x: x[1], reverse=True)])
    ttuxiaoshuo.append([i[0] for i in sorted([[i, j] for i, j in Counter(txiaoshuo).items()], key=lambda x: x[1], reverse=True)])
    ttucate.append([i[0] for i in sorted([[i, j] for i, j in Counter(tcates).items()], key=lambda x: x[1], reverse=True)])


f1(d2014,2014)
f1(d2015,2015)
f1(d2016,2016)
f1(d2017,2017)
# 摘取第一年前十个类别和小说
tencate = tucate[0][:10]
tenxiaoshuo = tuxiaoshuo[0][:10]
tend = {}
# 显示中文
plt.rcParams['font.sans-serif'] = ['SimHei']
# 定义X轴
x_axix = ['2014','2015','2016','2017']
# 定义颜色列表
colors = ['green','red','blue','yellow','pink','black','purple','grey','lime','indigo']
# 找出每个类别在每年的排名
aw = 5
for i in tencate:
    tend[i] = []
    for j in tucate:
        try:
            if j.index(i) + 1 > 20:
                tend[i].append(20)
            else:
                tend[i].append(j.index(i) + 1)
        except:
            tend[i].append(aw)
            aw += 1
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
ax = plt.gca()
# 因为是排序 倒序y轴
ax.invert_yaxis()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.title('图书馆大数据')
colorn = 0
# 将每一个类别作为一条单独的折现画图
for i in tend.keys():
    plt.plot(x_axix, tend[i], color=colors[colorn], label=i,marker='*')
    plt.text(x_axix[-1], tend[i][-1], '    ' + i, ha='left', va='bottom', fontsize=10)

    colorn += 1
plt.xlabel('年度')
plt.yticks(range(1,11))

plt.ylabel('排名')
plt.show()
# 下面将学生类别改为教师类别 学生小说 教师小说即可，原理相同
tend = {}
aw = 5
for i in tenxiaoshuo:
    tend[i] = []

    for j in tuxiaoshuo:
        try:
            if j.index(i) + 1 > 20:
                tend[i].append(20)
            else:
                tend[i].append(j.index(i) + 1)
        except:
            tend[i].append(aw)
            aw += 1
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
ax = plt.gca()
ax.invert_yaxis()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.title('图书馆大数据')

colorn = 0
for i in tend.keys():
    plt.plot(x_axix, tend[i], color=colors[colorn], label=i,marker='*')
    plt.text(x_axix[-1], tend[i][-1], '    ' + i, ha='left', va='bottom', fontsize=10)

    colorn += 1
plt.xlabel('年度')
plt.yticks(range(1,11))

plt.ylabel('排名')
plt.show()
tencate = ttucate[1][:10]
tenxiaoshuo = ttuxiaoshuo[1][:10]
tend = {}
aw = 5
for i in tencate:
    tend[i] = []

    for j in ttucate:
        try:
            if j.index(i)+1 > 20:
                tend[i].append(20)
            else:
                tend[i].append(j.index(i) + 1)
        except:
            tend[i].append(aw)
            aw += 1
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
ax = plt.gca()
ax.invert_yaxis()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.title('图书馆大数据')
colorn = 0
for i in tend.keys():
    plt.plot(x_axix, tend[i], color=colors[colorn], label=i,marker='*')
    plt.text(x_axix[-1], tend[i][-1], '    ' + i, ha='left', va='bottom', fontsize=10)

    colorn += 1
plt.xlabel('年度')
plt.yticks(range(1,11))

plt.ylabel('排名')
plt.show()
tend = {}
aw = 5
for i in tenxiaoshuo:
    tend[i] = []

    for j in ttuxiaoshuo:
        try:
            if j.index(i)+1 > 20:
                tend[i].append(20)
            else:
                tend[i].append(j.index(i) + 1)
        except:
            tend[i].append(aw)
            aw += 1
plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
ax = plt.gca()
ax.invert_yaxis()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.title('图书馆大数据')
colorn = 0
for i in tend.keys():
    plt.plot(x_axix, tend[i], color=colors[colorn], label=i,marker='*')
    plt.text(x_axix[-1], tend[i][-1], '    ' + i, ha='left', va='bottom', fontsize=10)

    colorn += 1
plt.xlabel('年度')
plt.yticks(range(1,11))

plt.ylabel('排名')
plt.show()
