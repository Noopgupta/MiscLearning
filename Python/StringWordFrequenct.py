# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 21:03:51 2025

@author: Admin
"""

s = "Noopur loves India-Noopur"

import re

words = re.split(r'[- ]', s)
print(words)

dict = {}

for word in words:
    if word in dict:
        dict[word] += 1
    else:
        dict[word] = 1
    
print(dict)