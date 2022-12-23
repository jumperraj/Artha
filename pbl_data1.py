#!/usr/bin/env python
# coding: utf-8

# **PBL project**

# In[10]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[11]:


df =pd.read_csv(r'C:/pbl/abhi4.csv')
df.head()


# In[12]:





# In[13]:


df.describe()


# In[14]:


ls =  df.min()

ls2= df.mean()
mean=ls2[0]
# In[35]:


stag=int(ls[0])
expense=ls2[0]-ls[0]


# defining the stagnant amount
# 

# In[16]:


arr1 = df.loc[:,'Amount']
arr2 = df.loc[:,'repayment']


# In[17]:


arr3 = arr1-arr2


# In[18]:



# In[19]:





# In[20]:





# In[21]:





# In[22]:





# In[23]:


df = df.assign(difference = arr3)


# In[24]:




# we have to definne a monthly statement

# In[25]:


df.sort_values(by=['Date-Time'],inplace = True)



# In[26]:


df.reset_index(drop=True,inplace=True)


# In[27]:




# In[44]:


arr3=arr3/100
arr4 =np.arange(4000)
list1= list(arr3)
def graph():
    plt.plot(list1)
    plt.ylabel("transaction amount (/100)")
    plt.xlabel("transaction frequency")
    plt.grid()
    plt.show()



# In[45]:






# In[30]:





# In[31]:



# In[37]:





