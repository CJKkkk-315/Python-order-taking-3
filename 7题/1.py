students = [{'SID':'103', 'Python': 93, 'Economics':95, 'English':91},
         {'SID':'101', 'Python': 85, 'Economics':83, 'English':86},
         {'SID':'102', 'Python': 73, 'Economics':72, 'English':74}]
scores = {}
for student in students:
    scores[student['SID']] = [student['Python'],student['Economics'],student['English']]
l = []
for i in scores.keys():
    l.append([i]+scores[i])
l.sort()
for i in l:
    print(i[0],':',i[1:])


s = input('请输入一个字符串：')
c = input('请输入用于填充的字符[如@、*、#等]：')
while True:
    l = input('请输入要显示的字符串的总长度[正整数]：')
    try:
        l = int(l)
        break
    except:
        print('输入有误，请重新输入！')
start = (l - len(s))//2
end =  l - len(s) - start
print(c*start+s+c*end)

from random import randint
d1 = {'一等奖':[0,0.1],'二等奖':[0.1,0.35],'三等奖':[0.35,1]}
d2 = {}
l = []
for i in range(2000):
    l.append(randint(0,99)/100)
for i in l:
    for j in d1.keys():
        if i >= d1[j][0] and i < d1[j][1]:
            d2[j] = d2.get(j,0) + 1
print(d2)


products = [['Iphone', 6888], ['MacPro', 14800], ['Huawei', 3499],['Coffee', 31],['Book', 80],['Nike Shoes', 799]]
print('=======商品列表=======')
for i,j in enumerate(products):
    print(i+1,j[0],j[1])
print('=====================')
car = []
m = 0
while True:
    n = input('请输入想要购买的商品编号，q为退出：')
    if n == 'q':
        break
    car.append(products[int(n)-1][0])
    m += products[int(n)-1][1]
for i in car:
    print(i)
print(f'此次购物的花费合计是:{m}元')

from random import randint
hole = [0,0,0,0,0]
hole[randint(0,4)] = 1
flag = 1
for i in range(10):
    n = int(input('请输入要抓的洞口（1-5）：'))
    if hole[n-1] == 1:
        print('成功啦')
        flag = 0
        break
    for i in range(len(hole)):
        if hole[i] == 1:
            hole[i] = 0
            t = i+(-1)**randint(1,2)
            if t < 0:
                t = 4
            elif t == 5:
                t = 0
            hole[t] = 1
if flag:
    print('失败啦')


day = int(input('请输入上班天数：'))
dis = float(input('请输入单程距离：'))
s = 0
sn = 0
if dis <= 6:
    m = 3
elif 6 < dis <= 12:
    m = 4
elif 12 < dis <= 22:
    m = 5
elif 22 < dis <= 32:
    m = 6
else:
    m = 6 + (dis - 32) // 20 + 1
for i in range(day*2):
    if 150 > s > 100:
        s += m*0.8
    elif 400 > s > 150:
        s += m*0.5
    else:
        s += m
    sn += m
print('使用费用为：')
print(round(s,2))
print('不使用费用为：')
print(round(sn,2))


with open('record.txt','r',encoding='utf8') as f:
    data = f.readlines()
head = data[0].replace('\n','').split(',')[1:]
d = {'左臂压差':[],'右臂压差':[]}
for line in data[1:]:
    l = line.replace('\n','').split(',')[1:]
    for i,j in zip(head,l):
        if i in d:
            d[i].append(int(j))
        else:
            d[i] = [int(j)]
    d['左臂压差'].append(int(l[0])-int(l[1]))
    d['右臂压差'].append(int(l[2]) - int(l[3]))
heart = sum(d['心率'])//len(d['心率'])
res = [['对比项','左臂','右臂']]
res.append(['高压最大值',max(d['左臂高压']),max(d['右臂高压'])])
res.append(['低压最大值',max(d['左臂低压']),max(d['右臂低压'])])
res.append(['高压平均值',sum(d['左臂高压'])//len(d['左臂高压']),sum(d['右臂高压'])//len(d['右臂高压'])])
res.append(['低压平均值',sum(d['左臂低压'])//len(d['左臂低压']),sum(d['右臂低压'])//len(d['右臂低压'])])
res.append(['压差平均值',sum(d['左臂压差'])//len(d['左臂压差']),sum(d['右臂压差'])//len(d['右臂压差'])])
r = 0
l = 0
for i in res:
    print('{:<10}{:<10}{:<10}'.format(i[0],i[1],i[2]))
for i in res[1:]:
    if i[1] > i[2]:
        l += 1
    else:
        r += 1
if r > l and r > 2:
    print(f'结论：右臂血压偏高, 心率的平均值为{heart}')
elif l > r and l > 2:
    print(f'结论：左臂血压偏高, 心率的平均值为{heart}')
else:
    print(f'结论：左臂血压与右臂血压相当, 心率的平均值为{heart}')


