from sklearn.datasets import load_iris # примеры данных 
from sklearn import tree # модуль для деревьев
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data.xlsx', index_col=0, comment='#')
# print(df[df.columns[0:3]])
# print(df.iloc[:, 0:3])
X= df.iloc[:, 0:3].values.tolist()
print(X)

# iris = load_iris() # загружаем данные
# X=iris.data # примеры входов
# y=iris.target # метки (примеры выходов)

# clf = tree.DecisionTreeClassifier() # создаем классификатор на основе дерева
# clf = clf.fit(X, y) # обучаем его, т.е. создаем само дерево

# # plot tree
# plt.figure(figsize=(12,12))
# tree.plot_tree(clf) # отображаем
# plt.show()