from sklearn.datasets import load_iris # примеры данных 
from sklearn import tree # модуль для деревьев
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_excel('data.xlsx', index_col=0, comment='#')
X= df.iloc[:, 0:4].values.tolist()
y= df.iloc[:, 4:5].values.tolist()

clf = tree.DecisionTreeClassifier() # создаем классификатор на основе дерева
clf = clf.fit(X, y) # обучаем его, т.е. создаем само дерево

# plot tree
plt.figure(figsize=(12,12))
tree.plot_tree(clf, filled=True) # отображаем
plt.show()

from sklearn.tree import export_text # подключаем функцию
r = export_text(clf) # переводим дерево в текстовую строку
print(r) # печатаем

res= clf.predict([[165, 84, 95, 95]]) #сюда подставить свои праметры
#Рост (см)	Вес (кг)	Сколько ехать до Стромынки (в минутах)	Сколько ехать до ЮЗ (в минутах)
print (res)
# ответ