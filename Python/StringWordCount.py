# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 13:32:25 2025

@author: Admin
"""

s = "I love my India-Noopur"

# Solution1
# s1 = s.split()
# print(len(s1))


# Solution2
# count = 1
# for i in s:
#     if i == " ":
#         count += 1
    
# print(count)


# Solution3
# Suppose " " and "-" are counted in word seperator

word_seperator = [" ", "-"]
count = 1
for i in s:
    if i in word_seperator:
        count += 1
        
print(count)