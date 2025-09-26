# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 20:40:17 2025

@author: Admin
"""

a = [1, 1, 2, 3, 6, 4]
sum = 10

# Solution 1
#for i in range(len(a)):
#    for j in range(len(a)):
#       if j > i and a[i]+a[j] == sum:
#            print(i,j)
#            break
            
 
# Solution 2
# a = sorted(a)

# i = 0
# j = len(a)-1

# while j > i:
#     if a[i] + a[j] > sum:
#         j -= 1
#     elif a[i] + a[j] < sum:
#         i += 1
#     else:
#         print(i,j)
#         break




# Solution 3

a = [1, 10, 2, 3, 6, 4]
sum = 6

d = {val:i for i, val in enumerate(a)}
print(d)


for i in range(len(a)):
    if sum - a[i] in d:
        print(i, d[sum - a[i]])
        break


# for i in range(len(a)):
#     if d.get(sum - a[i]) is not None:
#         print(i, d[sum - a[i]])
#         break




























