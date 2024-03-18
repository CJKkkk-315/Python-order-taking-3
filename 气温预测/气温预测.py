# 导入包
import pandas as pd
# 读取csv数据集
df = pd.read_csv('QingDao2020-22.csv',encoding='gbk')
# 将时间转为列表
date = df['当地时间'].values.tolist()
# 将时间字符串提取成年月日 小时
hour = [int(i.split(' ')[1].split(':')[0]) for i in date]
year = [int(i.split(' ')[0].split('.')[2]) for i in date]
mouth = [int(i.split(' ')[0].split('.')[1]) for i in date]
day = [int(i.split(' ')[0].split('.')[0]) for i in date]
# 转为一个4列的dataframe
x = {'year':year,'mouth':mouth,'day':day}
x = pd.DataFrame(x)
print(x)
# 将平均气温提取成y因变量
y = df['平均气温']
print(y)
# 引入数据集分隔
from sklearn.model_selection import train_test_split
# 分隔训练集和测试集 8:2分隔
train_x, test_x, train_y, test_y = train_test_split(x,y,test_size=0.25,random_state=42)
# 引入随机森林回归
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators=1000,random_state=42)
# 利用训练集和测试集拟合
rf.fit(train_x,train_y)
from sklearn import metrics
# 预测
y_pred = rf.predict(test_x)
# 计算精确度
print('Accuracy:', metrics.explained_variance_score(test_y, y_pred))


# 实际预测
year = int(input('请输入预测年份:'))
mouth = int(input('请输入预测月份:'))
day = int(input('请输入预测日期:'))
# hour = int(input('请输入预测小时:'))
pre = {'year':[year],'mouth':[mouth],'day':[day]}
y_pred = rf.predict(pd.DataFrame(pre))
print('预测温度为：',y_pred[0])
