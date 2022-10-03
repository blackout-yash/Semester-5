# -*- coding: utf-8 -*-

# -- Sheet --

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sn

data = pd.read_csv("tips.csv")
data.head()

plt.scatter(data['day'], data['tip'])
plt.title('scatterplot')
plt.xlabel('day')
plt.ylabel('tip')

plt.scatter(data['day'], data['tip'], c = data['total_bill'], s = data['size'])
plt.xlabel('day')
plt.ylabel('tip')

plt.colorbar()
plt.show()

plt.bar(data['day'], data['tip'])
plt.title('scatterplot')
plt.xlabel('day')
plt.ylabel('tip')

plt.show()

plt.hist(data['day'])
plt.title('histogram')
plt.show()

sn.scatterplot(x = 'day', y = 'tip', data = data)
plt.show()

sn.scatterplot(x = 'day', y = 'tip', data = data, hue = 'sex')
plt.show()

sn.lineplot(x = 'day', y = 'tip', data = data)
plt.show()

sn.barplot(x = 'day', y = 'tip', data = data, hue = 'sex')
plt.show()

sn.histplot(x = 'day', data = data, hue = 'size', kde = True)
plt.show()

