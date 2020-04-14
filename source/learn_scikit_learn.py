from sklearn import svm
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
#from sklearn.cross_validation import train_test_split


iris = datasets.load_iris()

print(type(iris))
print(iris.data)
print(iris.feature_names)

print(iris.target)
print(iris.target_names)

X = iris.data
Y = iris.target
print(X.shape)
print(Y.shape)
knn = KNeighborsClassifier(n_neighbors=1)
print(knn)
knn.fit(X,Y)
a = np.array([4,5,6,2])
print(knn.predict([a]))

from sklearn.linear_model import LogisticRegression
logReg = LogisticRegression()
logReg.fit(X,Y)
print("---")
print(logReg.predict([a]))


