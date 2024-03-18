import pandas as pd
xls = pd.read_excel('Assignment_Data.xlsx',sheet_name='CHN144',header=None)
data = xls.values.tolist()
writer = pd.ExcelWriter('Assignment_Data.xlsx', engine='openpyxl')
xls.to_excel(excel_writer=writer, sheet_name='CHN144', encoding="GBK",index=None,header=None)
def distance(x1,x2,y1,y2):
    return round(((x1-x2)**2+(y1-y2)**2)**0.5,2)
res = [[distance(i[1],j[1],i[2],j[2]) for j in data] for i in data]
Distance = {}
Distance['城市'] = [i[0] for i in data]
for i,j in zip([i[0] for i in data],res):
    Distance[i] = j
df1 = pd.DataFrame(Distance)
df1.to_excel(excel_writer=writer, sheet_name='Distance', encoding="GBK",index=None)
sd = []
for i in data:
    t = sorted(Distance[i[0]])[1]
    r = [[i[0] for i in data][Distance[i[0]].index(t)],t]
    sd.append(r)
Shortest_Distance = {}
Shortest_Distance['城市'] = [i[0] for i in data]
Shortest_Distance['最邻近的城市'] = [i[0] for i in sd]
Shortest_Distance['距离'] = [i[1] for i in sd]
sortten = []
for i,j,k in zip(Shortest_Distance['城市'],Shortest_Distance['最邻近的城市'],Shortest_Distance['距离']):
    sortten.append([i,j,k])
sortten.sort(key=lambda x:x[2])
Shortest_Distance['最近'] = [sortten[i][0]+'  '+sortten[i][1] for i in range(0,20,2)]
nsortten = sortten[::-1]
Shortest_Distance['最远'] = [nsortten[i][0]+'  '+nsortten[i][1] for i in range(0,20,2)]
for i in range(len(Shortest_Distance['最近']),len(Shortest_Distance['城市'])):
    Shortest_Distance['最近'].append(' ')
    Shortest_Distance['最远'].append(' ')
df2 = pd.DataFrame(Shortest_Distance)
df2.to_excel(excel_writer=writer, sheet_name='Shortest_Distance', encoding="GBK",index=None)
writer.save()
writer.close()
s = [i[0] for i in sortten[:10]] + [i[1] for i in sortten[:10]]
l = [i[0] for i in nsortten[:10]] + [i[1] for i in nsortten[:10]]
cc = []
for i in data:
    if i[0] in s:
        cc.append('short')
    elif i[0] in l:
        cc.append('long')
    else:
        cc.append('normal')
xls['cc'] = cc
import turtle
a = [[i[0],i[1]/7-300,i[2]/7-200] for i in data]
turtle.setup(600,400,0,0)
turtle.pensize(10)
turtle.speed(0)
turtle.up()
for m in a:
    if m[0] in s:
        turtle.pencolor("pink")
    elif m[0] in l:
        turtle.pencolor("blue")
    else:
        turtle.pencolor("black")
    turtle.goto(m[1],m[2])
    turtle.down()
    turtle.goto(m[1],m[2])
    turtle.up()
turtle.done()
import plotly_express as px
px.scatter(xls, x=1, y=2,color='cc').show()
