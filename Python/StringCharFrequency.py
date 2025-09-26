# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 21:16:28 2025

@author: Admin
"""

# Print the frequency of each character in a string, in frequency-wise order.

s = "I love my India-Noopur"

# Solution1
# dict = {}

# for i in s:
#     if i in dict:
#         dict[i] += 1
#     else:
#         dict[i] = 1
        
# print(dict)


# Solution2

# from collections import Counter

# freq = dict(Counter(s))
# print(freq)


# Solution3

freq = {char: s.count(char) for char in set(s)}
print(freq.items())



# Sorting the dictionary

# Sol1
sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
print(sorted_freq)


# Sol2

# def get_value(item):
#     return item[1]

# sorted_items = sorted(freq.items(), key=get_value, reverse=True)
# sorted_freq = dict(sorted_items)
# print(sorted_freq)

string = ''
stringOccurance = ''

for i in sorted_freq.items():
    string = string + str(i[0])
    stringOccurance = stringOccurance + str(i[1])

print(string)
        
print(stringOccurance)
    




