# Key with the Highest Value
# Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.
#
# Example:
#
# my_dict = {'a': 5, 'b': 9, 'c': 2}
# max_value_key(my_dict))
# Output:
#
# b

my_dict = {'a': 5, 'b': 9, 'c': 2}
print(max(my_dict, key=my_dict.get)) # b
# print(max(my_dict)) # c




my_dict = {'a': 5, 'b': 9, 'c': 2}
# sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
sorted_dict = dict(sorted(my_dict.items(), reverse=True))

first_key = next(iter(sorted_dict))
first_value = sorted_dict[first_key]
print(first_key, first_value)