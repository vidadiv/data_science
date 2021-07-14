#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[2]:


url = "https://www.vidadiv.com/blog"
text = requests.get(url).text
soup = BeautifulSoup(text,"html5lib")

all_urls = [a['href']
           for a in soup('a')
           if a.has_attr('href')]
print(len(all_urls))


# In[5]:


print(all_urls)


# In[6]:


import re


# In[15]:


regex = r"https://www.vidadiv.com/post/*"
assert re.match(regex, "https://www.vidadiv.com/post/diálogos-con-el-vacuonavegante-ii")
assert re.match(regex, "https://www.vidadiv.com/post/d%C3%ADa-29-el-mundo-cada-7-d%C3%ADas")
assert re.match(regex, "https://www.vidadiv.com/post/pálido-punto-azul")
assert not re.match(regex, "www.vidadiv.com/post/pálido-punto-azul")
assert not re.match(regex, "https://www.vidadiv.com/blog/lo-que-hemos-dejado-de-ver")


# In[16]:


good_urls = [url for url in all_urls if re.match(regex,url)]
print(len(good_urls))


# In[17]:


print(good_urls)


# In[18]:


good_urls = list(set(good_urls))
print(len(good_urls))


# In[19]:


from typing import Dict, Set


# In[20]:


def paragraph_mentions(text: str, keyword:str)->bool:
    """
    Returns True if a <p> inside the text mentions {keyword}
    """
    
    soup = BeautifulSoup(text,'html5lib')
    paragraphs = [p.get_text() for p in soup('p')]
    
    return any(keyword.lower() in paragraph.lower()
                for paragraph in paragraphs)


# In[21]:


text = """<body><h1>Facebook</h1><p>Twitter</p>"""
assert paragraph_mentions(text,"twitter")
assert not paragraph_mentions(text,"facebook")


# In[32]:


for bl_link in good_urls:
        url = f"{bl_link}"
        text = requests.get(url).text
        
        if paragraph_mentions(text,'pandemia'):
            print(f"{bl_link}")
            #break #done with this bl_url 


# In[ ]:




