# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 14:12:20 2025

@author: Admin
"""

# Count the total number of characters in a string, excluding spaces.

s = "I love my India-Noopur"

count = 0
chars_to_exclude = [" ", "-"]

for i in s:
    if i not in chars_to_exclude:
        count += 1
        
print(count)