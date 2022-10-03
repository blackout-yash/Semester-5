# -*- coding: utf-8 -*-

# -- Sheet --

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np

df = pd.read_csv("housing.csv")
# df = df.dropna()

df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.fillna(999, inplace=True)

np.any(np.isnan(df))

df.head()
df.describe

df.plot.scatter('RM', 'MEDV')

x = df[['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']]
y = df['MEDV']

# print(type(x))
# print(type(y))

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.4)

lm = LinearRegression()
lm.fit(X_train, y_train)

predictions = lm.predict(X_test)

plt.scatter(y_test, predictions)
plt.xlabel('y_test')
plt.ylabel('prediction')
plt.show()

from sklearn import metrics

print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

sns.distplot((y_test-predictions), bins = 50)

coefficients = pd.DataFrame(lm.coef_, x.columns)
coefficients.columns = ['coefficients']
coefficients

