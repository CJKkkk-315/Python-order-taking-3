import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['simhei']

#读取数据，丢弃缺失值
df = pd.read_csv('data.csv', encoding='cp936')
df = df.dropna()

#生成并保存营业额折线图
plt.figure()
df.plot(x='日期')
plt.savefig('first.jpg')

#按月统计，生成并保存柱状图
plt.figure()
from copy import deepcopy
df1 = deepcopy(df)
# df1['month'] = df1['日期'].map(lambda x: x[:x.rindex('-')])
df1['month'] = df1['日期'].str.slice(0,7)
df1 = df1.groupby(by='month', as_index=False).sum()
df1.plot(x='month', kind='bar')
plt.savefig('second.jpg')

#查找涨幅最大的月份，写入文件
df2 = df1.drop('month', axis=1).diff()
print(df2)
m = df2['销量'].nlargest(1).keys()[0]
with open('maxMonth.txt', 'w') as fp:
    fp.write(df1.loc[m, 'month'])

#按季度统计，生成并保存饼状图
plt.figure()
one = df1[:3]['销量'].sum()
two = df1[3:6]['销量'].sum()
three = df1[6:9]['销量'].sum()
four = df1[9:12]['销量'].sum()
plt.pie([one, two, three, four],
        labels=['one', 'two', 'three', 'four'])
plt.savefig('third.jpg')