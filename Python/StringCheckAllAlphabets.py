# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 17:53:30 2025

@author: Admin
"""

# Two strings are said to be complete if on concatenation, they contain all the 26 English alphabets. 
# For example, “abcdefghi” and “jklmnopqrstuvwxyz” are complete as they together have all characters from ‘a’ to ‘z’. 
# We are given two sets of sizes n and m respectively and we need to find the number of pairs that are complete 
# on concatenating each string from set 1 to each string from set 2



import string
alphabet_set = set(string.ascii_lowercase)

string1= "abcdefghi"
string2 = "jklmnopqrstuvwxyz"

str = string1 + string2
for i in alphabet_set:
    if str.__contains__(i):
        pass
    else:
        print("No")
        break