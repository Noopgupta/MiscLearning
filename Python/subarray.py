import numpy as np

# Find a Subarray of two numbers which has sum 100
# Array [10, 23, 89, 11]
# Answer - [89, 11]



# arr = np.array([10, 23, 89, 11])
# vals_dict = {}
#
# for i in range(len(arr)):
#     vals_dict[arr[i]] = 100-arr[i]
#
# print(vals_dict)
#
# vals_list = list(vals_dict.keys())
#
# for i in vals_dict:
#     if vals_dict[i] in vals_list:
#         print(i, vals_dict[i])
#         break
#

#
# 10, 23, 89, 11, 0
#
# 10+23=33
# 100-33 = 67
#

# if 89 > 67
#     then 23 + 89 = 112
#     100 - 112 = -12
#
# 89 + 10 = 99
#
#
#
# 100-(10+23) = 67
# 67+89 = 133
# 133-100 ---> 33 (10+23) -->
#
# 0, 10, 11, 15, 20 ,23, 89, 0 --> 168





# Find a Subarray which has sum 100

# Array [10, 23, 89, 11, 0]
# Return all combinations which give sum of 100
#
# Answer - [89, 11, 0]

# import numpy as np
# arr = np.array([10, 23, 89, 11, 0])
# arr = np.sort(arr)
# print(arr)
#
# n = len(arr)
# sum_val = 0
#
#
# for i in range(n-1, -1, -1):
#     for j in range(n-1, 1, 1):
#         print(f"Index: {j}, Value: {arr[j]}")


# list = [10, 23, 89, 11, 0]
# target_sum = 100
# [0, 10, 11, 23, 89]
# step1- binary search target or closest element smaller then target_sum
# step2- 100-89 = 11, if 0 then check if we have 0 in list add numbers,0 in result list, remove 89 else go to step1
# with target_sum 11
# step3-



