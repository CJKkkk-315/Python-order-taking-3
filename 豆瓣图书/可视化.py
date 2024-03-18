import matplotlib.pyplot as plt
import csv
import sqlite3
conn = sqlite3.connect('book.db')
from collections import Counter
c = conn.cursor()
print("数据库打开成功")

results = c.execute("SELECT *  from BOOK")
resultList = []

for result in results:
    resultList.append(result)
conn.close()
plt.rcParams['font.sans-serif'] = ['SimHei']

res = [i[7] for i in resultList]
d = sorted(Counter(list(res)).items())
x = [i[0] for i in d]
y = [i[1] for i in d]
plt.title('评分/数量')
plt.bar(x,y)
plt.show()

res = [i[4]-i[4]%10 for i in resultList if i[4] < 150]
d = sorted(Counter(list(res)).items())
x = [i[0] for i in d]
y = [i[1] for i in d]
plt.title('价格/数量')
plt.plot(x,y)
plt.show()
res = [i[5][:4] for i in resultList if i[5][:4].isdigit() and len(i[5][:4]) == 4]
print(res)
d = sorted(Counter(list(res)).items())
x = [i[0] for i in d]
y = [i[1] for i in d]
plt.title('时间/数量')
plt.xticks(rotation=30)
plt.plot(x,y)
plt.show()