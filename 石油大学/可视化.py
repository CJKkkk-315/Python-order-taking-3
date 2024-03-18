import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
data = []
# 读入爬取到的原始数据
with open('origin_data.txt','r',encoding='utf8') as f:
    for i in f.readlines():
        data.append(i.replace('\n','').split(','))
print(data)
# 利用字典分类不同民族
d = {}
for i in data:
    d[i[2]] = d.get(i[2],0) + 1
huatu = []
for i,j in d.items():
    if i:
        huatu.append([j,i])
huatu.sort()
huatu = huatu[::-1]
# 提取xy轴
x = []
y = []
for i in huatu[:10]:
    x.append(i[1])
    y.append(i[0])
# 绘图
plt.bar(x,y)
plt.title('民族人数排名')
plt.show()
# 剩下2张分析也是同理
d = {}
for i in data:
    d[i[5]] = d.get(i[5],0) + 1
huatu = []
for i,j in d.items():
    huatu.append([j,i])
huatu.sort()
huatu = huatu[::-1]
x = []
y = []
for i in huatu[:10]:
    x.append(i[1])
    y.append(i[0])
plt.pie(labels=x,x=y)
plt.title('婚姻状况占比')
plt.show()


huatu = []
for i in data:
    huatu.append([i[4],i[5]])
x = []
y = []
huatu.sort()
for i in huatu:
    x.append(i[0])
    y.append(i[1])

plt.scatter(x,y)
plt.title('身高和婚姻状况关系')
plt.xticks(rotation=60)
plt.show()

