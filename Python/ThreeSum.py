# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 21:15:33 2025

@author: Admin
"""

a = [1, 10, 2, 3, 6, 4]
sum = 6

d = {val:i for i, val in enumerate(a)}
print(d)

found = False

# for i in range(0,len(a)):
#     for j in range(i+1,len(a)):
#         for k in range(j+1,len(a)):
#             if a[i]+a[j]+a[k] == sum:
#                 print(i,j,k)
#                 break


for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if sum - a[i]- a[j] in d:
            print(i,j,d[sum - a[i]- a[j]])
            found = True
            break
    if found == True:
        break