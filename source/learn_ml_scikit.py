import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = pd.read_csv('listings-Odie-Pichappan.csv')
print(data.shape)
print(data.head())
X = data['reviews_per_month'].values
Y = data['price'].values
X = X.reshape((48864,1))
reg = LinearRegression()
reg = reg.fit(X,Y)
Y_pred = reg.predict(X)
mse = mean_squared_error(Y, Y_pred)
rmse = np.sqrt(mse)
r2_score = reg.score(X,Y)
print(np.sqrt(mse))
print(r2_score)

# %matplotlib inline
#import seaborn as sns
#from sklearn.ensemble import RandomForestClassifier
#from sklearn.svm import SVC
#from sklearn import svm
#from sklearn.neural_network import MLPClassifier
#from sklearn.metrics import confusion_matrix, classification_report
#from sklearn.preprocessing import StandardScaler, LabelEncoder
#from sklearn.model_selection import train_test_split
#loading dataset
#wine = pd.read_csv('winequality-red.csv', sep=';')
#print(wine)