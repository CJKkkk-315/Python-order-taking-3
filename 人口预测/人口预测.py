import pandas as pd
import numpy as np

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
df = pd.read_excel('内蒙古人口.xlsx')
year = df['年份'].tolist()
number = df['常住人口(万人)'].tolist()
pre = [2025,2030,2040,2050]
data = []
for i,j in zip(year,number):
    if str(j) != 'nan':
        data.append([i,j])
year = [i[0] for i in data]
start_year = min(year)
number = [i[1] for i in data]
ly = len(year)
ln = len(number)
lp = len(pre)
train_x = np.array(year).reshape([ly,1])
train_y = np.array(number)
test_x = np.array(pre).reshape([lp,1])
from sklearn.preprocessing import PolynomialFeatures
model = PolynomialFeatures(degree=2)
x_model = model.fit_transform(train_x)
lin_reg = LinearRegression()
lin_reg.fit(x_model,train_y)
plt.scatter(train_x,train_y,c='red')
all_x = np.arange(1949,2050).reshape([-1,1])
plt.plot(all_x,lin_reg.predict(model.fit_transform(all_x)))
plt.show()
test_x = model.fit_transform((test_x))
for i,j in zip([2025,2030,2040,2050],lin_reg.predict(test_x)):
    print(f'预测{i}年的人口为：{j}')
year = df['年份'].tolist()
number = df['老年(%)'].tolist()
pre = [2025,2030,2040,2050]
data = []
for i,j in zip(year,number):
    if str(j) != 'nan':
        data.append([i,j])
year = [i[0] for i in data]
start_year = min(year)
number = [i[1] for i in data]
ly = len(year)
ln = len(number)
lp = len(pre)
train_x = np.array(year).reshape([ly,1])
train_y = np.array(number)
test_x = np.array(pre).reshape([lp,1])
model = PolynomialFeatures(degree=2)
x_model = model.fit_transform(train_x)
lin_reg = LinearRegression()
lin_reg.fit(x_model,train_y)
plt.scatter(train_x,train_y,c='red')
all_x = np.arange(start_year,2050).reshape([-1,1])
plt.plot(all_x,lin_reg.predict(model.fit_transform(all_x)))
plt.show()
test_x = model.fit_transform((test_x))
for i,j in zip([2025,2030,2040,2050],lin_reg.predict(test_x)):
    print(f'预测{i}年的老龄率为：{j}')

year = df['年份'].tolist()
number = df['儿童(%)'].tolist()
pre = [2025,2030,2040,2050]
data = []
for i,j in zip(year,number):
    if str(j) != 'nan':
        data.append([i,j])
year = [i[0] for i in data]
start_year = min(year)
number = [i[1] for i in data]
ly = len(year)
ln = len(number)
lp = len(pre)
train_x = np.array(year).reshape([ly,1])
train_y = np.array(number)
test_x = np.array(pre).reshape([lp,1])
model = PolynomialFeatures(degree=2)
x_model = model.fit_transform(train_x)
lin_reg = LinearRegression()
lin_reg.fit(x_model,train_y)
plt.scatter(train_x,train_y,c='red')
all_x = np.arange(start_year,2050).reshape([-1,1])
plt.plot(all_x,lin_reg.predict(model.fit_transform(all_x)))
plt.show()
test_x = model.fit_transform((test_x))
for i,j in zip([2025,2030,2040,2050],lin_reg.predict(test_x)):
    print(f'预测{i}年的儿童率为：{j}')