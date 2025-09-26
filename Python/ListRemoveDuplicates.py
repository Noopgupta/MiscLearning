# list = [1, 1, 2, 2, 3, 4, 5]
# Output : [1, 2, 3, 4, 5]

list1 = [1, 1, 2, 2, 3, 4, 5]
# print(list(set(list1)))

unique = set()
print([x for x in list1 if not (x in unique or unique.add(x))])


# def remove_duplicates(lst):
#     seen = set()
#     result = []
#     for item in lst:
#         if item not in seen:
#             seen.add(item)
#             result.append(item)
#     return result
#
#
# print(remove_duplicates(list1))