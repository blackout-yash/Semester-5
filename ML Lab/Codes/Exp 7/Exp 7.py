# -*- coding: utf-8 -*-

# -- Sheet --

import pandas as pd

df = pd.read_csv("data.csv")
print(df)

# Mapping categorical values to numerical value 


d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)
d = {'YES': 1, 'NO': 0}
df['Go'] = df['Go'].map(d)
print(df)

features = ['Age', 'Experience', 'Rank', 'Nationality']

x = df[features]
y = df['Go']

print(x)
print(y)

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt

dtree = DecisionTreeClassifier()
dtree = dtree.fit(x,y)

tree.plot_tree(dtree, feature_names=features)

# **Predicting the Values**


print(dtree.predict([[40, 10, 7, 1]]))

print(dtree.predict([[40, 10, 6, 1]]))

