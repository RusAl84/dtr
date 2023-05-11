# from sklearn.datasets import load_iris # примеры данных 
from sklearn import tree # модуль для деревьев
from sklearn.ensemble import RandomForestClassifier # случайный лес
import matplotlib.pyplot as plt

import pandas as pd

df = pd.read_excel('data.xlsx', index_col=0, comment='#')
X= df.iloc[:, 0:4].values.tolist()
y= df.iloc[:, 4:5].values.tolist()

# clf = tree.DecisionTreeClassifier() # создаем классификатор на основе дерева

num_tree =3
clf = RandomForestClassifier(max_depth=5,# 5 максимальная глубина дерева
                            n_estimators=num_tree,# 5 число деревьев в лесу
                            max_features=4)# максимальное число признаков для каждого дерева
clf = clf.fit(X, y) # обучаем его, т.е. создаем само дерево
#TODO
#fdfd fddffd 


# plot tree
# for i in range(num_tree):
#     tree_data=clf.estimators_[i] 
#     plt.figure(figsize=(12,12))
#     tree.plot_tree(tree_data, filled=True) # отображаем
#     plt.show()

res= clf.predict([[178, 96, 45, 90]]) #сюда подставить свои праметры
#Рост (см)	Вес (кг)	Сколько ехать до Стромынки (в минутах)	Сколько ехать до ЮЗ (в минутах)
print (res[0])
# ответ