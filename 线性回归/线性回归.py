import pandas as pd
import numpy as np

def function(target):
    print('当前回归：',target)
    data_before = pd.read_excel("回归.xlsx")
    total = data_before.isnull().sum().sort_values(ascending=False)
    data_before = data_before[[target,'X1','X2','X3','X4','X5','X6']]
    data = data_before.drop(data_before[data_before[target].isnull()].index)
    x1 = np.array(data['X1'])
    x2 = np.array(data['X2'])
    x3 = np.array(data['X3'])
    x4 = np.array(data['X4'])
    x5 = np.array(data['X5'])
    x6 = np.array(data['X6'])
    y_income = np.array(data[target])
    x = range(1, len(x1) + 1)
    Y = y_income.T
    X = np.array([list(x) for x in zip(np.ones(len(y_income)), x1, x2, x3, x4, x5, x6)])
    B = np.matmul(np.matmul(np.linalg.inv(np.matmul(X.T, X)), X.T), Y)
    print("回归方程为 y = %f + %fx1 + %fx2 + %fx3 + %fx4 + %fx5 + %fx6" % (B[0], B[1], B[2], B[3], B[4], B[5], B[6]))
    y_predict = B[0] + B[1] * x1 + B[2] * x2 + B[3] * x3 + B[4] * x4 + B[5] * x5 + B[6] * x6
    y1 = np.sum((y_predict - np.mean(y_income)) ** 2)
    y2 = np.sum((y_income - np.mean(y_income)) ** 2)
    R1 = y1 / y2
    print("可决系数R^2=", R1)
for target in ['众壹资产稳健套利1号日利率','日出定向1号日利率','中邮永安景上源1号日利率','道合东哥1号私募证券投资基金日利率']:
    function(target)