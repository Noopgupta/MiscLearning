t1 = 'a', 'b', 'c'
t2= ('a', 'b', 'c')

t3 = ('a')
t4 = ('a',)  # one element tuple declaration
# print(t1)
# print(t2)
# print(t3)
# print(t4)
#
# t5 = tuple('abc')
# print(t5)
# #
# print(t1 + t2)
# print(t4 * 5)
# print('b' in t1)
# print('d' in t1)
# print(t1.count('a'))
# print(t1.index('a'))
# print(len(t4))
# print(max(t1))
# print(tuple([1,2,3,4]))
# print(list(t1))
#
# t6 = ([1,2],[3,4])
# print(t6)

#
# init_tuple = ()
# print (init_tuple.__len__())
# #
# init_tuple_a = 'a', 'b'
# init_tuple_b = ('a', 'b')
#
# print(init_tuple_a == init_tuple_b)

# init_tuple_a = '1', '2'
# init_tuple_b = ('3', '4')
#
# print(init_tuple_a + init_tuple_b)

# init_tuple_a = 1, 2
# init_tuple_b = (3, 4)
#
# [print(sum(x)) for x in [init_tuple_a + init_tuple_b]]

# init_tuple = [(0, 1), (1, 2), (2, 3)]
# result = sum(n for _, n in init_tuple)
# print(result)

# init_tuple is a list of tuples: [(0, 1), (1, 2), (2, 3)].
# A generator expression is used inside the sum() function: n for _, n in init_tuple.
#     This expression iterates through each tuple in init_tuple and extracts the second element of each
#     tuple (denoted by n), discarding the first element (denoted by _).
#     The generator expression produces the following sequence of values: 1, 2, 3.
#     The sum() function calculates the sum of the generated values: 1 + 2 + 3, which is 6.
#     result is assigned the value 6. print(result) prints the value of result, which is 6.