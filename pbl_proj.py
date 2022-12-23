#!/usr/bin/env python
# coding: utf-8

# **PBL project**

# In[10]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[11]:


df =pd.read_csv(r'/abhi4.csv')
df.head()


# In[12]:


df.corr()


# In[13]:


df.describe()


# In[14]:


ls =  df.min()
print(ls)


# In[35]:


stag=ls[0]
print(stag)


# defining the stagnant amount
# 

# In[16]:


arr1 = df.loc[:,'Amount']
arr2 = df.loc[:,'repayment']


# In[17]:


arr3 = arr1-arr2


# In[18]:


arr3


# In[19]:


arr1
arr2
arr3


# In[20]:


arr1


# In[21]:


arr2


# In[22]:


arr3


# In[23]:


df = df.assign(difference = arr3)


# In[24]:


df.head()


# we have to definne a monthly statement

# In[25]:


df.sort_values(by=['Date-Time'],inplace = True)



# In[26]:


df.reset_index(drop=True,inplace=True)


# In[27]:


df.head()


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


graph()
arr4 = df.loc[:,'Sender_name']
arr4


# In[30]:


df['Sender_name'].mask(df['Sender_name']=="june",inplace=True)



# In[31]:


df


# In[36]:


df["Sender_name"]= df["Sender_name"].str.replace("june", "", case = False)


# In[37]:





