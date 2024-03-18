# -*- coding: utf-8 -*-
"""
Created on Wed Jul  
@author: raoxi
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def tran(r1):
    #用于将对应序号转化为时间
    r2=r1*0.6
    return r2
def trans(r1):
    #用于将时间转化为序号
    r2=r1*10
    r3=r2/6
    return r3
# 读取数据
file_name='1.xlsx'
pd.read_excel(file_name)
data2=pd.read_excel(file_name,header=0)
data3=pd.read_excel(file_name,sheet_name=1,header=0)
df=pd.read_excel(file_name,sheet_name=2)
data1=df.iloc[:,-1:]   #选取最后一列数据
##### fig=plt.figure(1)#定义画布

# 三个表的绘制
fig,ax=plt.subplots(nrows=1,ncols=3,figsize=(12,4))
plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False
x=np.arange(41779)
y=np.arange(41779)
z=np.arange(41756)
x1=tran(x)
y1=tran(y)
z1=tran(z)
# #plt.plot(z,data3,color='b',ls='-',label='物理量3')
# 分块绘制
x=y=np.linspace(0,41779,41779)
z=np.linspace(0,41756,41756)
ax[0].set_title("物理量1")
ax[0].plot(x1,data1,color="g",ls='-',label="物理量1")
ax[0].legend(loc='upper left')
ax[1].set_title("物理量2")
ax[1].plot(y1,data2,color="r",ls='-',label="物理量2")
ax[1].legend(loc='upper left')
ax[2].set_title("物理量3")
ax[2].plot(z1,data3,color="b",ls='-',label="物理量3")
ax[2].legend(loc='upper left')
plt.show( )

# #查找物理量二的最大值极其对应时间
data2.idxmax()
m=list(data2.idxmax().index)
m1=float(data2.idxmax().values)*0.6
print("物理量2的最大值",m)
print("时间为",m1,"s")

# #查询
q=int(input("选择要查询的物理量（输入1,2,3即可）="))
if q==1:
    data=data1
    a1=int(input("时间范围（低）"))
    a2=int(input("时间范围（高，小于25067）"))
elif q==2:
    data=data2
    a1=int(input("时间范围（低）"))
    a2=int(input("时间范围（高，小于25067）"))
elif q==3:
    data=data3
    a1=int(input("时间范围（低）"))
    a2=int(input("时间范围（高，小于25053）"))
b1=int(trans(a1))
b2=int(trans(a2))
datan=data.iloc[b1:b2,0:1]
b3=int(b2-b1)
k=np.linspace(a1,a2,b3)
fig=plt.figure()#定义画布，必须要用
plt.rcParams["font.sans-serif"]=["SimHei"]
plt.rcParams["axes.unicode_minus"]=False
plt.plot(k,datan,color='k',ls='-',label='区段检测')

#峰值
#sheet_name为sheet索引
data = pd.read_excel(r'1.xlsx',sheet_name=0,header=None)
train_data = np.array(data)  # np.ndarray()
excel_list = train_data.tolist()  # list
list1 = []
for i in range(len(excel_list)):
    list1.append(excel_list[i][0])
max_value = max(list1)






















