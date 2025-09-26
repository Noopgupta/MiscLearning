# Elementwise Sum
# Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.
#
# Example
#
# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# output_tuple = tuple_elementwise_sum(tuple1, tuple2)
# print(output_tuple)  # Expected output: (5, 7, 9)

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)



print(tuple(map(sum, zip(tuple1, tuple2))))

#
# Or
#
if len(tuple1) != len(tuple2):
    raise ValueError("Input tuples must have the same length.")

result = tuple(a + b for a, b in zip(tuple1, tuple2))
print(result)


Or

output_tuple = []
for i in range(len(tuple1)):
    output_tuple.append(tuple1[i] + tuple2[i])


output_tuple = tuple(output_tuple)
print(output_tuple)