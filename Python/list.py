import numpy as np

# All list operations are same as array operations, same functions work

list1 = ['a', 'b', 'c', 'd', 'e']
list2 = ['f', 'g', 'a']
list3 = [1, 2, 3, 11, 8, 6]
# list3.remove(6)
# print(list3)

# print(list1 + list2)
# print(list1 * 2)

# print(len(list1))
# print(max(list1))
# print(min(list1))
# print(sum(list3))

# a = "n"
# b = list(a)
# print(b)
#
# a = "n n n m"
# b = a.split()
# print(b)
#
# a = "n-n-n-m"
# delimiter = '-'
# b = a.split(delimiter)
# print(b)
#
# a = "spam-spam-spam"
# delimiter = 'a'
# b = a.split(delimiter)
# print(b)
# print(delimiter.join(b))
# print(type(delimiter.join(b)))


# list3 = list3 + [10]
# print(list3)
#
# list3 = list3.append([10]) # doesn't work this way
# print(list3)

# print(list3)
#
# print(sorted(list3)) # Doesn't sort the original list
# print(list3)
#
# list3.sort() # Sorts the original list
# print(list3)


# Difference between array and list-Numeric functions can be done on arrays, not list

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


# List Comprehensions

# prev_list = [1, 2, 3]
# new_list = [i*2 for i in prev_list]
# print(new_list)
#
# new_list = [i for i in prev_list]
# print(new_list)
#
# language = 'Python'
# lan = [letter for letter in language]
# print(lan)

# for i in language:
#     print(i)

# prev_list = [-1, 2, -3, 4]
# new_list = [i*2 for i in prev_list if i > 0]
# print(new_list)
#
# new_list = [i*i for i in prev_list if i < 0]
# print(new_list)


# a=[1,2,3,4,5]
# print(a[3::-1])
# print(a[3:0:-1])
# print(a[3:1:-1])
# print(a[3:0:-2])
# print(a[3:0:-3])
# print(a[3:0:-4])
# print(a[3:0:-5])

#
# a=[1,2,3,4,5,6,7,8,9]
# print(a[::2])
#
# arr = [1, 2, 3, 4, 5, 6]
# for i in range(1, 6):
#     arr[i - 1] = arr[i]
# for i in range(0, 6):
#     print(arr[i], end = " ")

# for i in range(0, 6):
#     print(i)
# for i in range(6):
#     print(i)
#
#
# arr = [[1, 2, 3, 4],
#        [4, 5, 6, 7],
#        [8, 9, 10, 11],
#        [12, 13, 14, 15]]
# for i in range(0, 4):
#     print(arr[i])
#     print(arr[i].pop())
#     print(arr[i])


# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60
# print(a) #ValueError: attempt to assign sequence of size 6 to extended slice of size 5


# import random
# fruit=['apple', 'banana', 'papaya', 'cherry']
# random.shuffle(fruit)
# print(fruit)

# data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
#
#
# def fun(m):
#     v = m[0][0]
#
#     for row in m:
#         for element in row:
#             print(element)
#             if v < element: v = element
#
#     return v
#
#
# print(fun(data[0]))


# def f(value, values):
#     v = 1
#     values[0] = 44
# t = 3
# v = [1, 2, 3]
# f(t, v)
# print(t, v[0])

# fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
# fruit_list2 = fruit_list1  #['Guava', 'Berry', 'Cherry', 'Papaya']
# fruit_list3 = fruit_list1[:] #['Apple', 'Kiwi', 'Cherry', 'Papaya']
#
#
# fruit_list2[0] = 'Guava'
# fruit_list3[1] = 'Kiwi'
#
# sum = 0
# for ls in (fruit_list1, fruit_list2, fruit_list3):
#     if ls[0] == 'Guava':
#         sum += 1
#     if ls[1] == 'Kiwi':
#         sum += 20
#
# print(sum)


# nums = [10, 20, 30, 40, 50]
#
# for index, value in enumerate(nums):
#     print(f"Index: {index}, Value: {value}")

# myList2D= [[1,2,3],[4,5,6],[7,8,9]]
# print(myList2D)
# print(len(myList2D))

# sum = 0
# for i in range(len(myList2D)):
#     print(i, myList2D[i][i], sum)
#     sum = sum + myList2D[i][i]
#
# print(sum)