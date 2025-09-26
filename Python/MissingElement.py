my_list = [1, 3, 3, 4, 4, 4]

i = 0
counts = {}
for elem in my_list:
    if elem in counts:
        counts[elem] += 1
    else:
        counts[elem] = 1

for key, value in counts.items():
    print(key, value)

# from collections import Counter
#
# my_list = [1, 3, 3, 4, 4, 4]
#
# # Use Counter to count the occurrences of each element
# element_counts = Counter(my_list)
# print(element_counts)
#
# for key, value in element_counts.items():
#     if value > 1:
#         print(key)


# elements = (4, 3, 2, 5, 5)
#
# for i in range(1, max(elements)+1):
#     if i not in elements:
#         print(i)

# elements = (1, 3, 5, 9, 7)
# min = 0
# max = 0
# sorted_elems = sorted(elements)
# print(sorted_elems)
#
# sum_element = 3
# for i in range(0, len(sorted_elems)-sum_element+1):
#     min = min + sorted_elems[i]
#     max = max + sorted_elems[len(sorted_elems) - 1 - i]
#
#
# print(min, max)