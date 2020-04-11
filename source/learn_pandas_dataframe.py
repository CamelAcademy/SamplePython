import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")

web_data = {"Day":[1,2,3,4,5,6], "Visitors":[1000,700,6000,1000,400,350], "Bounce":[20,30,23,15,10,34]}
df = pd.DataFrame(web_data)
print(df)
print(df.head(2)) # Slicing
print(df.tail(3))
################
df1 = pd.DataFrame({"HPI":[80,90,70,60],"Int_Rate":[2,1,2,3], "IND_GDP":[50,45,45,67]},
                   index = [2001, 2002, 2003, 2004])
df2 = pd.DataFrame({"HPI":[80,90,70,60],"Int_Rate":[2,1,2,3], "IND_GDP":[50,45,45,67]},
                   index = [2005, 2006, 2007, 2008])
#merge = pd.merge(df1, df2)
merge = pd.merge(df1, df2, on = "HPI") # merge 2 dataframe
print(merge)
print("Concat")
Concat = pd.concat([df1,df2])
################
df1 = pd.DataFrame({"HPI":[80,90,70,60],"Int_Rate":[2,1,2,3], "IND_GDP":[50,45,45,67]},
                   index = [2001, 2002, 2004, 2007])
df2 = pd.DataFrame({"Age":[80,90,70,60],"RF_Rate":[2,1,2,3], "World_GDP":[50,45,45,67]},
                   index = [2001, 2002, 2013, 2005])

joined = df1.join(df2)
print(joined)
####################
web_data = {"Day":[1,2,3,4,5,6], "Visitors":[1000,700,6000,1000,400,350], "Bounce":[20,30,23,15,10,34]}
df = pd.DataFrame(web_data)
df = df.rename(columns={"Visitors":"Users"})
df.set_index("Day", inplace = True)
df.plot()
print(df)
plt.show()

