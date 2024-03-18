import pandas as pd
# 读取初始数据，转换为列表
xls = pd.read_excel('Assignment_Data.xlsx',sheet_name='CHN144',header=None)
data = xls.values.tolist()
res = []
# 两两之间计算距离，存放至res列表
for i in data:
    aw = []
    for j in data:
        aw.append(round(((i[1]-j[1])**2+(i[2]-j[2])**2)**0.5,2))
    res.append(aw)
d = {}
dmin = {}
short = []
long = []
# 初始化d字典
d['城市'] = [i[0] for i in data]
dmin['城市'] = [i[0] for i in data]
# d字典用来存放每个城市到别的城市的距离
for i,j in zip([i[0] for i in data],res):
    d[i] = j
res = []
# 找出每个城市最领巾的城市以及距离
for i in data:
    t = sorted(d[i[0]])[1]
    r = [[i[0] for i in data][d[i[0]].index(t)],t]
    res.append(r)
dmin['最邻近的城市'] = [i[0] for i in res]
dmin['距离'] = [i[1] for i in res]
sl10 = []
# 找出最临近的10个城市和相离最远的十个城市
for i,j,k in zip(dmin['城市'],dmin['最邻近的城市'],dmin['距离']):
    sl10.append([i,j,k])
sl10.sort(key=lambda x:x[2])
for i in sl10[:10]:
    short.append(i[0])
    short.append(i[1])
for i in sl10[::-1][:10]:
    long.append(i[0])
    long.append(i[1])
# 定义color列表，方便后续画图使用
color = []
for i in data:
    if i[0] in short:
        color.append('short')
    elif i[0] in long:
        color.append('long')
    else:
        color.append('normal')
# 将最近最远转换为 城市-城市的形式方便存储
dmin['最近'] = [sl10[i][0]+'-'+sl10[i][1] for i in range(0,len(sl10[:20]),2)]
dmin['最远'] = [sl10[::-1][:20][i][0]+'-'+sl10[::-1][:20][i][1] for i in range(0,len(sl10[::-1][:20]),2)]
# 填充字典使得每个值与别的值一样长，才可以转换为dataframe
while True:
    dmin['最近'].append('')
    dmin['最远'].append('')
    if len(dmin['最远']) == len(dmin['城市']):
        break
# 转换为dataframe 使用pandas写入sheet
df1 = pd.DataFrame(d)
df2 = pd.DataFrame(dmin)
writer = pd.ExcelWriter('Assignment_Data.xlsx', engine='openpyxl')
xls.to_excel(excel_writer=writer, sheet_name='CHN144', encoding="GBK",index=None,header=None)
df1.to_excel(excel_writer=writer, sheet_name='Distance', encoding="GBK",index=None)
df2.to_excel(excel_writer=writer, sheet_name='Shortest_Distance', encoding="GBK",index=None)
writer.save()
writer.close()
# 将x坐标y坐标都除以10，再将y坐标取反 用turtle库画图
import turtle
a = [[i[0],i[1]/10,i[2]/10] for i in data]
turtle.setup(800,400,0,0)
turtle.pensize(10)
turtle.speed(0)
turtle.up()
for m in a:
    if m[0] in short:
        turtle.pencolor("red")
    elif m[0] in long:
        turtle.pencolor("green")
    else:
        turtle.pencolor("black")
    turtle.goto(m[1],-m[2])
    turtle.down()
    turtle.goto(m[1],-m[2])
    turtle.up()
turtle.done()
# 定义新的颜色列，同时将y取反，利用plotly_express库画图
xls[3] = color
import plotly_express as px
xls['y'] = -xls[2]
px.scatter(xls, x=1, y='y',color=3).show()
