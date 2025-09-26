# c = ['a', 'b', 'c']
# b = (1, 2, 3)
# print(type(c))
# print(type(b))

import array as arr
import numpy as np

# creating an array with integer type and traverse
arr1 = arr.array('i', [1, 2, 3, 4, 5])
arr2 = arr.array('f', [1.2, 2, 3, 4, 5])
arr3 = arr.array('d', [1.1, 21.0, 3.3, 4.8, 5])
arr4 = arr.array('u', ['a', 'b', 'c', 'd', 'e'])
mylist = ['a', 'b', 'c', 'd', 'e']

# print(type(arr1))
# print(arr2)
# print(arr3)
# print(arr4)
#
# print(arr1)
#
# for i in arr1:
#     print(i)
#     print(arr1[i-1])
#

# for j in range(len(arr4)):
#     print(j)
#     print(arr4[j])

# print(arr4[0])


# def array_traversal_index(array, index):
#     if index >= len(array):
#         print("Index out of bounds")
#     else:
#         print(array[index])
#
#
# array_traversal_index(arr4, 2)
# array_traversal_index(arr4, 5)
# array_traversal_index(arr4, 4)
#
# print(arr4)
# arr4.append('g')
# print(arr4)
# # print(arr4[5])
#
# arr4.insert(4, 'h')
# print(arr4)
# arr4.insert(-1, 'x')
# print(arr4)
# # arr4.insert('y')
# # print(arr4)
# arr4.insert(0, 'z')
# print(arr4)
# print(arr4[-1])
#
# arr4.append('w')
# print(arr4)
#
#
# arr5 = arr.array('u', ['j', 'k', 'l', 'm', 'n'])
# arr4.extend(arr5)
# print(arr4)
#
# list1 = ['a', 'b', 'c']
# arr4.fromlist(list1)
# print(arr4)


# arr4.pop()
# arr4.pop(2)
# print(arr4)

# arr4.remove('b')
# print(arr4)

# print(arr4.index('d'))

# arr4.reverse()
# print(arr4)

# print(arr4.buffer_info())
# # O/P-- (2670164394416, 5)-- it says that arr4 starts from 2670164394416 and has 5 elements

# print(arr4.count('a'))
# arr4.append('a')
# print(arr4.count('a'))

# print(type(arr4))
# print(arr4.tolist())
# print(type(arr4))

# print(arr4)
# print(arr4[1:4])
# # prints from 1st index to 3rd not 4th
#
# print(arr4[1:])
# print(arr4[:4])
# print(mylist)
# # del mylist[2]
# del mylist[2:4]

# print(mylist)

# Delete works on index, remove works on value

# Remove Element
# nums = [0,1,2,2,3,0,4,2]
# val = 2
# l = len(nums)
# i = 0
# while i < l:
#     print("Before:", i, nums[i], l)
#     if nums[i] == val:
#         nums.remove(val)
#         l = l-1
#         i = i-1
#     i = i+1
#
#
# print(nums)


# Merge Sorted Array

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# for i in range(n):
#     nums1[m+i] = nums2[i]
#
# nums1.sort()


# nums = [1, 1, 2]
#
# Remove duplicates in same array then return length of array
# def removeDuplicates(self, nums: List[int]) -> int:
#     s = sorted(list(set(nums)))
#     nums.clear()
#     for i in s:
#         nums.append(i)
#     return len(nums)

# OR
    # new_array = []
    # for i in nums:
    #     if i not in new_array:
    #         new_array.append(i)
    #
    # nums.clear()
    # nums.extend(new_array)
    # return len(nums)
# OR
#     nums[:] = sorted(set(nums))
#         return len(nums)

# nums = sorted(set(nums)) doesn't overwrite array/list. nums[:] does **********************************
#         return len(nums)


# Keep 2 occurrences of a value, each unique element appears at most twice.
# nums = [1, 1, 1, 2, 2, 3]
# nums = [0,0,1,1,1,1,2,3,3]
# l = len(nums)
# i = 0
# while i < l-2:
#     print(i, l)
#     if nums[i] == nums[i+1] & nums[i] == nums[i+2]:
#         nums.remove(nums[i+2])
#         l = l-1
#     else:
#         i = i+1
#
# print(nums)
# OR
# for i in nums:
#     while( nums.count(i)>2):
#         nums.remove(i)
#     else:
#         nums
# return len(nums)
#
# nums = [1, 2, 2, 3, 3, 3, 4, 5]
# element = 3
# count = nums.count(element)
# print(f"The element {element} appears {count} times in the list.")


# Difference between array and list- Numeric functions can be done on arrays, not list

# arr11 = np.array([1, 2, 3, 4, 5])
# list11 = [1, 2, 3, 4, 5]
#
# print(arr11/2)
# print(list11/2)

# arr12 = np.array([1, 2, 3, 4, 5, 'a']) # All will be converted to string, won't be integer anymore. so data type would be same, string in this case
# print(arr12)
#
# list12 = [1, 2, 3, 4, 5,'a'] # All will not be converted to string, so data type would be integer and string respectively
# print(list12)
