#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt


# In[8]:


random_2d_array = np.random.rand(50, 2)
flattened_array = random_2d_array.flatten()


# In[9]:


random_2d_array


# In[10]:


flattened_array


# In[11]:


plt.hist(flattened_array, bins=10, color='blue', alpha=0.7)
plt.title('Histogram of Random 2D Array')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()


# In[ ]:




