#!/usr/bin/env python
# coding: utf-8

# In[57]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[60]:


df = pd.read_csv('C:\\Users\dell\Downloads\\company_sales_data.csv')
df


# In[61]:


df.head()


# In[63]:


df.tail()


# In[64]:


df.describe()


# In[67]:


df.dtypes


# In[68]:


df.shape


# In[79]:


profitList = df ['total_profit'].tolist()
monthList  = df ['month_number'].tolist()
plt.plot(monthList, profitList, label = 'Month-wise Profit data of last year')
plt.xlabel('Month number')
plt.ylabel('Profit in dollar')
plt.xticks(monthList)
plt.title('Company profit per month')
plt.yticks([100000, 200000, 300000, 400000, 500000])
plt.show()


# In[121]:


monthList  = df ['month_number'].tolist()
bathingsoapSalesData   = df ['bathingsoap'].tolist()
plt.bar(monthList, bathingsoapSalesData)
plt.xlabel('Month Number')
plt.ylabel('Sales units in number')
plt.xticks(monthList)

plt.grid(True, linewidth= 1, linestyle="dotted")
plt.title('Bathingsoap sales data')

plt.show()


# In[124]:


labels = ['FaceCream', 'FaseWash', 'ToothPaste', 'Bathing soap', 'Shampoo', 'Moisturizer']
salesdata   = [df ['facecream'].sum(), df ['facewash'].sum(), df ['toothpaste'].sum(), 
         df ['bathingsoap'].sum(), df ['shampoo'].sum(), df ['moisturizer'].sum()]
plt.axis("equal")
plt.pie(salesdata, labels=labels, autopct='%1.1f%%')
plt.legend(loc='center left')
plt.title('Sales data')
plt.show()


# In[122]:


df['total_profit'].sum()


# In[ ]:




