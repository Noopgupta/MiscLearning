# -*- coding: utf-8 -*-
"""
Created on Thu Jul 24 18:27:10 2025

@author: Admin
"""

str = "    Hello      World     "

print(str.strip(' '))

print(''.join(str.split()))

print(' '.join(str.split()))


# new_str = ''

# prev_char = ''


# for i in str:
#     if i == ' ' and prev_char != ' ' and prev_char != i:
#         new_str = i + new_str
#         prev_char = i
#     elif i == ' ' and prev_char == ' ':
#         prev_char = i
#     elif i != ' ' and  prev_char != i:
#         new_str = i + new_str
#         prev_char = i
#     elif i != ' ' and  prev_char == i:
#         new_str = i + new_str
#         prev_char = i
           
# print(new_str)


# for i in range(len(str)):
#     if i == 0 and str[i] == ' ':
#         prev_char = str[i]
#     elif i == len(str)-1 and str[i] == ' ':
#         break
#     elif str[i] == ' ' and prev_char != ' ' and prev_char != str[i]:
#         new_str = str[i] + new_str
#         prev_char = str[i]
#     elif str[i] == ' ' and prev_char == ' ':
#         prev_char = str[i]
#     elif str[i] != ' ' and  prev_char != str[i]:
#         new_str = str[i] + new_str
#         prev_char = str[i]
#     elif str[i] != ' ' and  prev_char == str[i]:
#         new_str = str[i] + new_str
#         prev_char = str[i]
           
# print(new_str)

# new_str1 = ''
# for i in range(len(new_str)): 
#     if i != 0:
#         new_str1 = new_str1 + new_str[i]

# print(new_str1)
    