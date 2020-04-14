
import pandas as pd


#df = pd.read_csv("app_info.csv", parse_dates=["LastUpdated"])
print(type(df.LastUpdated[0]))
#new_df = df.fillna(0)
#new_df = df.fillna({'Rating':999})
new_df = df.fillna(method="ffill") #bfill

df3 = df.dropna()
df3 = df.dropna(thresh=1)
df3 = df.dropna(how="all")
"""
df2 = df.interpolate(method="time")
df.set_index('Day',inplace=True)
#print(df)

#df.sort_values('App', ascending=False)
df.sort_values(['Category','Rating'], ascending=[0,0])

print(df.iloc[2])
#print(df.columns)
print(df['Category'][0:20])
print(df[['Category','App']])

#print(df.head(5))

print(df.describe())
print(df.iloc[2])
print(df.iloc[1:4])
print(df.iloc[1,2])


for index, row in df.iterrows():
    print(index, row[2])

file1 = pd.read_csv('C:\\Users\\pichappan\\Documents\\Odie\\WaltDisney\\ESPN_take_home\\app_info.csv')
df=file1.head(100)


import csv
file2 = open('C:\\Users\\pichappan\\Documents\\Odie\\WaltDisney\\ESPN_take_home\\app_info.csv', newline='')
reader = csv.reader(file2)
header = next(reader)
data = [row for row in reader]
print(header)
print(data[0])
"""

SELECT app_reviews.Sentiment, count(app_reviews.App)
FROM app_reviews
group by app_reviews.Sentiment
order by app_reviews.Sentiment

