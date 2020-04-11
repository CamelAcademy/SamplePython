import numpy as np
import pandas as p
import matplotlib.pyplot as plt

dataset = p.read_excel('ExpSalary.xlsx')
x = dataset.iloc[:,:-5].values
y = dataset.iloc[:,1].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25,random_state=0 )

from sklearn.linear_model import LinearRegression
simpleLinearRegression = LinearRegression()
simpleLinearRegression.fit(x_train, y_train)

y_predit = simpleLinearRegression.predict(x_test)
y_fly = simpleLinearRegression.predict([[11]])

#plt.scatter(x_train, y_train, color = 'red')
plt.scatter(x_test,simpleLinearRegression.predict(x_test), color = 'red')
plt.plot()