# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 20:30:45 2025

@author: Admin
"""

# Get highest frequency element
words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']

new_dict = {}.fromkeys(words, 0)

for i in words:
    new_dict[i] += 1
    
print(new_dict)

val = max(new_dict, key = new_dict.get)
print(val)