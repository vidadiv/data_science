#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import os
from tqdm import tqdm
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin, urlparse


# In[2]:


def is_valid(url):
    """
    Checks whether url is valid URL
    """
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


# In[8]:


def get_all_images(url):
    """
    Returns all image URLs on a single url
    """
    soup = bs(requests.get(url).content, "html.parser")
    urls=[]
    for img in tqdm(soup.find_all("img"), "Extracting images"):
        img_url = img.attrs.get("src")
        if not img_url:
            #if img does not contain src attribute just skip
             continue
        #make the URL absolute bu joining domain with URL that is just extacted
        img_url = urljoin(url, img_url)
        #remove URLs like weird endings
        try:
            pos = img_url.index("?")
            img_url = img_url[:pos]
        except ValueError:
            pass
        #if the url is valid
        if is_valid(img_url):
            urls.append(img_url)
    return urls


# In[9]:


def download(url, pathname):
    """
    Downloads a file given an URL and puts it in the forlder 'pathname'
    """
    #if path doesn't exist, make that path dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    #download the body of response by chunk, not immediately
    response = requests.get(url, stream=True)
    #get the total file size
    file_size = int(response.headers.get("Content-Lenght",0))
    #get the file name
    filename = os.path.join(pathname, url.split("/")[-1])
    #progress bar, changing the unit to bytes instead of iteration (default by tqdm)
    progress = tqdm(response.iter_content(1024),f"Downloading {filename}", total=file_size, unit="B", unit_scale = True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for data in progress.iterable:
            #write data read to the file
            f.write(data)
            #update the progress bar manually
            progress.update(len(data))


# In[10]:


def main(url,path):
    #get all images
    imgs = get_all_images(url)
    for img in imgs:
        #for each image, download it
        print(img)
        download(img,path)


# In[11]:


main("https://smfm.mx/galeria/","/Users/adiv/Dropbox/SMFMimages")


# In[ ]:




