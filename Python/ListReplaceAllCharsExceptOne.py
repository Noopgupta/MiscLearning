# Python program to Replace all Characters of a List Except the given character

# Given a List. The task is to replace all the characters of the list with N except the given character.
#
# Input : test_list = [‘G’, ‘F’, ‘G’, ‘I’, ‘S’, ‘B’, ‘E’, ‘S’, ‘T’], repl_chr = ‘*’, ret_chr = ‘G’
# Output : [‘G’, ‘*’, ‘G’, ‘*’, ‘*’, ‘*’, ‘*’, ‘*’, ‘*’]
# Explanation : All characters except G replaced by *

test_list = ['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T']
repl_chr = '*'
ret_chr = 'G'


# new_list = [i if i == ret_chr else repl_chr for i in test_list]
# print(new_list)

new_list = [i.replace(i, repl_chr) if i != ret_chr else ret_chr for i in test_list]
print(new_list)

# new_list = []
# for i in test_list:
#     if i == ret_chr:
#         new_list.append(i)
#     else:
#         new_list.append(repl_chr)
#
# print(new_list)

