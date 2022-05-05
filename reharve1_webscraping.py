# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 21:49:35 2022

@author: Rachel
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.zappos.com/men-loafers/CK_XARC21wHAAQLiAgMBAhg.zso?p='
data = pd.DataFrame(columns = ['Name','Price'])

for page in range(0,9):
    print('Page ' + str(page) + ' of 8')
    new_url = url + str(page)
    page_object = requests.get(new_url)
    parsed_page = BeautifulSoup(page_object.content , 'html.parser')
    element = parsed_page.find_all('dl' , class_ = 'ls-z')    
    for item in element:
            name = item.find('p', itemprop='name').text
            try:
                price = item.find('span', itemprop='price').text
                
            except:
                price = item.find('span', itemprop='price').next_sibling.text
   
            new_dress=pd.DataFrame(data=[[name , price]],columns=['Name','Price'])
            data=data.append(new_dress)
