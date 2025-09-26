# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 16:43:59 2025

@author: Admin
"""

str = "abcdef"

print(str[::-1])

print(str[2:len(str):1])


rev = ""

for i in str:
    rev = i + rev
    print(rev)
    
print(rev)
    

val = ''.join(reversed(str))
print(val)