import numpy as np
import pandas as p
from sklearn import linear_model
#import matplotlib.pyplot as plt

df = p.read_excel('HomeValue.xlsx')

import math
median_room1 = df.Room.median()
median_room2 = math.floor(df.Room.median())
df.Room = df.Room.fillna(median_room1)

from sklearn.linear_model import LinearRegression
mReg = LinearRegression()
mReg.fit(df[['Age','SqFt','Room','Bath','Pool']],df.Value)
coef = mReg.coef_
intercept = mReg.intercept_
y_predit = mReg.predict([[1.2, 2345, 3, 2, 0]])