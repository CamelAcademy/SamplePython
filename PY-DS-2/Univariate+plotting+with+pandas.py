
# coding: utf-8

# In[11]:


import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
reviews = pd.read_csv(r"C:\Users\George\Documents\biodiversity-in-national-parks\winemag-data-130k-v2.csv", index_col=0)
reviews.head(3)


# In[12]:


reviews['province'].value_counts().head(10).plot.bar()


# In[21]:


(reviews['province'].value_counts().head(10) / len(reviews)).plot.bar() #this is bar chartable


# In[ ]:


Bar charts are very flexible: The height can represent anything, as long as it is a number. And each bar can represent anything, as long as it is a category.

In this case the categories are nominal categories: "pure" categories that don't make a lot of sense to order. Nominal categorical variables include things like countries, ZIP codes, types of cheese, and lunar landers. The other kind are ordinal categories: things that do make sense to compare, like earthquake magnitudes, housing complexes with certain numbers of apartments, and the sizes of bags of chips at your local deli.


# In[22]:


reviews['points'].value_counts().sort_index().plot.bar() #find the points where by it is seen to be 80 - 100. (Bar chart)


# In[ ]:


When numbers get too large, we would be using bar chart anymore, we will use line graph


# In[23]:


reviews['points'].value_counts().sort_index().plot.line()


# In[ ]:


Let's do a quick exercise. Suppose that we're interested in counting the following variables:

The number of tubs of ice cream purchased by flavor, given that there are 5 different flavors. BAR
The average number of cars purchased from American car manufacturers in Michigan. LINE
Test scores given to students by teachers at a college, on a 0-100 scale. LINE
The number of restaurants located on the street by the name of the street in Lower Manhattan. BAR

Sometimes, your data will have too many points to do something "neatly", and that's OK.
If you organize the data by value count and plot a line chart over that, 
You'll learn valuable information about *percentiles*: that a street in the 90th percentile has 20 restaurants, 
for example, or one in the 50th just 6. This is basically a form of aggregation: 
we've turned streets into percentiles!


# In[24]:


reviews['points'].value_counts().sort_index().plot.area()


# In[25]:


reviews[reviews['price'] < 200]['price'].plot.hist() #using histogram, will be analyzing pokemon sets after this

reviews['province'].value_counts().head(10).plot.pie()

plt.gca().set_aspect('equal')

