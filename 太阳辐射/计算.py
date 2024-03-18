with open('2020太阳辐射数据.txt','r') as f:
    data = f.readlines()
Pclears = []
Pcloudys = []
for i in data[1:13]:
    a,b = i.split(',')
    Pclears.append(float(a))
    Pcloudys.append(float(b))
Mt = [i*0.7+j*0.3 for i,j in zip(Pclears,Pcloudys)]
Md = [i*0.2+j*0.7 for i,j in zip(Pclears,Pcloudys)]
BHIhs = [0 for i in range(12)]
DHIhs = [0 for i in range(12)]
for i in data[14:]:
    a,b,c,d,e,f = i.split(',')
    mouth = int(b.split('/')[1])
    BHIhs[mouth-1] += float(c)
    DHIhs[mouth-1] += float(d)
# print(BHIhs)
# print(DHIhs)
GHIr = sum([a*b + c*d for a,b,c,d in zip(BHIhs,Mt,DHIhs,Md)])
print(GHIr)
with open('面积数据.txt','r') as f:
    area = sum([float(i.replace('\n','')) for i in f.readlines()])
ASR = area * GHIr
print(ASR)
Paz = 140*area
print(Paz)
Ep = GHIr*(Paz/1000)*0.8
print(Ep)
with open('输出报告.txt','w',encoding='utf8') as f:
    f.write('太阳能光伏潜力报告\n')
    f.write(f'1、屋顶总面积:{area}m²\n')
    f.write(f'2、水平面实际接收到的太阳辐射GHI:{GHIr}W/m²\n')
    f.write(f'3、晴空条件光束水平辐射度BHI:{sum(BHIhs)}W/m²\n')
    f.write(f'4、晴空条件下漫反射水平辐射度DHI:{sum(DHIhs)}W/m²\n')
    f.write(f'5、屋顶表面的年太阳辐射ASR:{ASR}Wh\n')
    f.write(f'6、太阳能光伏潜力Ep:{Ep}Wh\n')
    f.write(f'7、当太阳能光伏板功率为100W时，则所需太阳能板个数为:{int(Ep//100)}\n')