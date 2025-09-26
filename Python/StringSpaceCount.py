# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 14:09:00 2025

@author: Admin
"""

# Count the total number of spaces in a given string

s = "I love my India-Noopur"
count = 0
chars_to_count = [" ", "-"]
for i in s:
    if i in chars_to_count:
        count += 1

print(count)