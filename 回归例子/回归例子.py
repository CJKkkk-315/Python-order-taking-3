from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
df = pd.read_csv('train.csv')
x = df.drop(['a+b'], axis=1)
y = df['a+b']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
model = MLPRegressor(max_iter=2000)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
print('Accuracy:', metrics.explained_variance_score(y_test, y_pred))
a = input('a:')
b = input('b:')
d = pd.DataFrame({'a':[a],'b':[b]})
y_pred = model.predict(d)
print(y_pred[0])
