

import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from collections import Counter
mpl.rcParams['font.sans-serif'] = ['STFangsong']
mpl.rcParams['font.serif'] = ['STFangsong']



data=pd.read_excel('111.xlsx')
Right=data['答案']
Answer=data['回答']
Subject=data['科目']

AnalyzeData=[]
for i in range(len(Right)):
    AnalyzeData.append((Subject[i].replace('高中','').replace('题库',''),Right[i],Answer[i]))

SW={}
for line in AnalyzeData:
    if line[1]!=line[2]:
        if not SW.get(line[0]):
            SW[line[0]]=0
        SW[line[0]]+=1
SX=[]
WN=[]
for k,v in SW.items():
    SX.append(k)
    WN.append(v)

plt.scatter(SX,WN,color='r')
plt.plot(SX,WN)
plt.title('高中各科错题具体数量')
for x, y in zip(SX, WN):
    plt.text(x, y + 0.3, '%.0f' % y, ha='center', va='bottom', fontsize=10.5)
plt.savefig('各科错题量.png')
plt.show()

#求一下错题率
STotal=Counter(Subject)
WPD={}
for k,v in SW.items():
    if STotal.get('高中'+k+'题库'):
        WPD[k]=v/STotal['高中'+k+'题库']
WP=[v for k,v in WPD.items()]

plt.scatter(SX,WP,color='r')
plt.plot(SX,WP)
plt.title('高中各科错题率')
for x, y in zip(SX, WP):
    plt.text(x, y + 0.003, '%.03f' % y, ha='center', va='bottom', fontsize=10.5)
plt.savefig('各科错题率.png')
plt.show()