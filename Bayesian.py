import pandas as pd
import numpy as np
from sklearn import datasets
iris = datasets.load_iris()
print(iris.data)
print(iris.target)
x = iris.data
y = iris.target
print(x.shape)
print(y.shape)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=9)

from sklearn.naive_bayes import GaussianNB
nv = GaussianNB()
print(nv.fit(x_train,y_train))

from sklearn.metrics import accuracy_score
y_pred = nv.predict(x_test)
print(accuracy_score(y_test,y_pred))
