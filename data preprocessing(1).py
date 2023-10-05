#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd
import numpy as np
import string
import re


# In[49]:


df=pd.read_csv("E://python_new//hotel ledger.csv")


# In[50]:


df


# In[51]:


# Remove rows with NaN values and non-informative rows
df = df.dropna(how='all').reset_index(drop=True)
df


# In[52]:


# Set the column headers to the values in Row 2
df.columns = df.iloc[2]


# In[53]:


df.columns


# In[55]:


# Remove rows with headers and non-informative rows
df1 = df[3:].reset_index(drop=True)
df1


# In[56]:


# Convert all columns to strings
df1 = df1.astype(str)

# Remove dollar signs and commas from all columns
df1 = df1.apply(lambda x: x.str.replace('[$,]', '', regex=True))




# In[57]:


df1


# In[77]:


row_access


# In[89]:


# Access a row by label (e.g., row with label 4)
row_label = 18
row_data = df1.loc[row_label]
row_data


# In[ ]:




