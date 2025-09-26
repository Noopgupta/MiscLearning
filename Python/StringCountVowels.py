# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 14:14:57 2025

@author: Admin
"""

# Count the total number of vowels (a, e, i, o, u) in a string


s = "I love my India-Noopur"


vowels = ['a', 'e', 'i', 'o', 'u']

count = 0
for i in s:
    if i in vowels:
        count += 1

print(count)