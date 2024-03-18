#-*- coding: utf-8 -*-
import pandas as pd
from sklearn.cluster import KMeans
import sklearn.preprocessing as sp
from pandas import DataFrame
import matplotlib.pyplot as plt
import csv
import sqlite3
from collections import Counter

conn = sqlite3.connect('book.db')
c = conn.cursor()
print("数据库打开成功")

results = c.execute("SELECT *  from BOOK")
resultList = []

for result in results:
    resultList.append(result)
conn.close()

df = DataFrame(resultList)
print(df.head())

# 绘制散点图 评分，参与评论人数
plt.figure(figsize=(10, 8))
plt.scatter(df[7].astype(float), df[8].astype(float))
plt.show()

scoreDf = pd.DataFrame(df, columns=[7])
k = 6  # 聚类的类别
iteration = 50000  # 聚类最大循环次数
model = KMeans(n_clusters=k,
               max_iter=iteration)  # 分为k类
model.fit(scoreDf)  # 开始对评分进行聚类
# 详细输出原始数据及其类别
res = pd.concat([df,
                 pd.Series(model.labels_, index=df.index)],
                axis=1)  # 详细输出每个样本对应的类别
res.columns = list(df.columns) + [u'class']  # 重命名表头
d = sorted(Counter(list(res['class'])).items())
x = [i[0] for i in d]
y = [i[1] for i in d]
plt.bar(x,y)
plt.show()
res.to_excel('评分聚类.xls')  # 保存结果


scoreDf = pd.DataFrame(df, columns=[8])
model = KMeans(n_clusters=k,
               max_iter=iteration)  # 分为k类
model.fit(scoreDf)  # 开始对评分进行聚类
# 详细输出原始数据及其类别
res = pd.concat([df,
                 pd.Series(model.labels_, index=df.index)],
                axis=1)  # 详细输出每个样本对应的类别
res.columns = list(df.columns) + [u'class']  # 重命名表头
d = sorted(Counter(list(res['class'])).items())
x = [i[0] for i in d]
y = [i[1] for i in d]
plt.bar(x,y)
plt.show()
res.to_excel('人气聚类.xls')  # 保存结果

scoreDf = pd.DataFrame(df, columns=[4])
model = KMeans(n_clusters=k,
               max_iter=iteration)  # 分为k类
model.fit(scoreDf)  # 开始对评分进行聚类
# 详细输出原始数据及其类别
res = pd.concat([df,
                 pd.Series(model.labels_, index=df.index)],
                axis=1)  # 详细输出每个样本对应的类别
res.columns = list(df.columns) + [u'class']  # 重命名表头
d = sorted(Counter(list(res['class'])).items())
x = [i[0] for i in d]
y = [i[1] for i in d]
plt.bar(x,y)
plt.show()
res.to_excel('价格聚类.xls')  # 保存结果

