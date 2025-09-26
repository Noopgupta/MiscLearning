def contains_duplicate(nums):
    unique = set()
    list1 = [x for x in nums if (x in unique or unique.add(x))]
    print(list1)
    if len(list1) > 1:
        return True
    else:
        return False


result = contains_duplicate([1, 2, 3, 1])
print(result)