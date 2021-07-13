#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys, re


# In[3]:


def get_domain(email_address: str) -> str:
    """Split on @ and return the last piece"""
    return email_address.lower().split("@")[-1]

#tests
assert get_domain('joelgrus@gmail.com') == 'gmail.com'
assert get_domain('joel@m.datascience.com') == 'm.datascience.com'


# In[ ]:


with open('email_addresses.txt', 'r') as f:
    domain_counts = Counter(get_domain(line.strip())
                    for line in f
                    if "@" in line)

