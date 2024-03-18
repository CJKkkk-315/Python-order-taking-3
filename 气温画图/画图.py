import matplotlib.pyplot as plt
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 读取数据
with open('tem_zj_yr.txt') as f:
    data = [i.replace('\n','').split() for i in f.readlines()][1:-1]
dataf = []
# 列表中添加年平均数据
for i in data:
    dataf.append([int(i[0]),float(i[1])])
# 滑动平均数据
huadong = [i for i in dataf[:5]]
# 计算滑动平均数据
for i in range(5,len(dataf)-5):
    res = round(sum([i[1] for i in dataf[i-5:i+6]])/11,2)
    huadong.append([dataf[i][0],res])
for i in range(len(dataf)-5,len(dataf)):
    huadong.append(dataf[i])
# 提取x,y轴
x = [i[0] for i in dataf]
y1 = [i[1] for i in dataf]
y2 = [i[1] for i in huadong]
# 设置画布
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(12,10))
# 画出11点滑动平均数据
line2 = axes.plot(x,y2, 'r', marker='o',label = '11点滑动平均')
# 画出年平均气温
line1 = axes.plot(x,y1, 'k', marker='o',label = '年平均气温')

axes.legend()
axes.set_title('1951-2021年湛江气温图')
plt.xlabel('年份/年')
plt.ylabel('气温/℃')
plt.show()