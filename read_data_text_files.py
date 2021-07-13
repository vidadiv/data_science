#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv


# In[5]:


with open('tab_delimited_stock_prices.txt') as f:
    tab_reader = csv.reader(f, delimiter = '\t')
    for row in tab_reader:
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])
        print(date," ",symbol," ",closing_price)


# In[6]:


with open('colon_delimited_stock_prices.txt') as f:
    colon_reader = csv.DictReader(f,delimiter=':')
    for dict_row in colon_reader:
        date = dict_row["date"]
        symbol = dict_row["symbol"]
        closing_price = float(dict_row["closing_price"])
        print(date," ",symbol," ",closing_price)


# In[7]:


today_prices = { 'AAPL' : 90.91, 'MSFT' : 41.68, 'FB' : 64.5 }


# In[8]:


with open('comma_delimited_stock_prices.txt','w') as f:
        writer = csv.writer(f, delimiter=',')
        for stock, price in today_prices.items():
            writer.writerow([stock, price])


# In[ ]:




