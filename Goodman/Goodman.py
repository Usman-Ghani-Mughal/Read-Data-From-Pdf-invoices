#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import tabula


# In[11]:


filename = 'Goodman_1'
dataframe_raw = tabula.read_pdf(filename+'.pdf')


# In[12]:


dataframe_raw.head(2)


# In[13]:


dataframe_raw.to_csv(filename+'.csv',header=True,index=None)

