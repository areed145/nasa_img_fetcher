# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 21:18:32 2016

@author: areed145
"""

from bs4 import BeautifulSoup
import urllib
import re

site = 'http://www.dfrc.nasa.gov'
subsite = '/Gallery/Photo'

top = 21
bot = 215

links = [a.get('href') for a in BeautifulSoup(urllib.request.urlopen(site+subsite).read()).find_all('a')]

links = links[top:bot]

sublinks = []
imglinks = []

for link in links:
    try:
        sublinks.extend([site+a.get('href') for a in BeautifulSoup(urllib.request.urlopen(site+subsite+'/'+link).read()).find_all('a', href=re.compile('/HTML/'))])
    except:
        pass
    
for sublink in sublinks:
    try:
        imglinks.extend([site+a.get('href') for a in BeautifulSoup(urllib.request.urlopen(sublink).read()).find_all('a', href=re.compile('/Large/'))])
    except:
        pass
    
for imglink in imglinks:
    if imglink[-3:] == 'jpg':
        try:
            urllib.request.urlretrieve(imglink, imglink.rsplit('/',1)[1])
        except:
            pass
    