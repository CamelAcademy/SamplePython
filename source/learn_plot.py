import pandas as pd
from matplotlib import pyplot as plt
#####################################
x = [1,3,5,6]
y = (3,2,7,3)
z = [12,14,16,11]
#plt.plot(x,y)
#plt.plot(x,z)
#plt.xlabel("Age")
#plt.ylabel("Income")
#plt.title("Age vs Income")
#plt.legend(["XvsY","XvsZ"]) # takes list as an arugment
#plt.show()
#####################################
sample_data = pd.read_csv("sample_data.csv")
print(sample_data)
print(type(sample_data))

print(sample_data.column_c)
print(type(sample_data.column_c))

print(sample_data.column_c.iloc[1])
print(type(sample_data.column_c.iloc[1]))

plt.plot(sample_data.column_a, sample_data.column_b, 'o')
plt.plot(sample_data.column_a, sample_data.column_c)
plt.show()
print("################################################")
data_all = pd.read_csv('countries.csv')
print(data_all)
data_us = data_all[data_all.country == 'United States']
data_india = data_all[data_all.country == 'India']
data_china = data_all[data_all.country == 'China']
print("#2###############################################")
print(data_us)
print(data_china)
print(data_india)
print(data_us.population.iloc[0])
#plt.plot(data_us.year, data_us.population/10**6)
plt.plot(data_us.year, data_us.population/data_us.population.iloc[0] * 100)
plt.plot(data_india.year, data_india.population/data_india.population.iloc[0] * 100)
plt.plot(data_china.year, data_china.population/data_china.population.iloc[0] * 100)
plt.legend(["USA","China", 'India'])
plt.xlabel("Year")
plt.ylabel('Population')
plt.title("Year vs Population")
plt.show()