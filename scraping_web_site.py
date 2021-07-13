#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests


# In[5]:


url = "https://www.house.gov/representatives"
text = requests.get(url).text
soup = BeautifulSoup(text,"html5lib")

all_urls = [a['href']
           for a in soup('a')
           if a.has_attr('href')]
print(len(all_urls))


# In[6]:


import re


# In[11]:


regex = r"^https?://.*\.house\.gov/?$"
assert re.match(regex, "http://joel.house.gov")
assert re.match(regex, "https://joel.house.gov")
assert re.match(regex, "http://joel.house.gov/")
assert re.match(regex, "https://joel.house.gov/")
assert not re.match(regex, "joel.house.gov")
assert not re.match(regex, "http://joel.house.com")
assert not re.match(regex, "https://joel.house.gov/biography")


# In[13]:


good_urls = [url for url in all_urls if re.match(regex,url)]
print(len(good_urls))


# In[14]:


good_urls = list(set(good_urls))
print(len(good_urls))


# In[16]:


html = requests.get("https://crow.house.gov").text
soup = BeautifulSoup(html,'html5lib')


# In[17]:


links = {a['href'] for a in soup('a') if 'press releases' in a.text.lower()}


# In[18]:


print(links)


# In[19]:


from typing import Dict, Set


# In[20]:


press_releases: Dict[str, Set[str]] = {}


# In[21]:


for house_url in good_urls:
    html = requests.get(house_url).text
    soup = BeautifulSoup(html, 'html5lib')
    pr_links = {a['href'] for a in soup('a') if 'press releases' in a.text.lower()}
    print(f"{house_url}:{pr_links}")
    press_releases[house_url] = pr_links


# In[25]:


def paragraph_mentions(text: str, keyword:str)->bool:
    """
    Returns True if a <p> inside the text mentions {keyword}
    """
    
    soup = BeautifulSoup(text,'html5lib')
    paragraphs = [p.get_text() for p in soup('p')]
    
    return any(keyword.lower() in paragraph.lower()
                for paragraph in paragraphs)


# In[26]:


text = """<body><h1>Facebook</h1><p>Twitter</p>"""
assert paragraph_mentions(text,"twitter")
assert not paragraph_mentions(text,"facebook")


# In[27]:


for house_url, pr_links in press_releases.items():
    for pr_link in pr_links:
        url = f"{house_url}/{pr_link}"
        text = requests.get(url).text
        
        if paragraph_mentions(text,'data'):
            print(f"{house_url}")
            break #done with this house_url 


# In[ ]:




