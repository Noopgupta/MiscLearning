# Concatenate
# Write a function that takes a tuple of strings and concatenates them, separating each string with a space.
#
# Example
#
# input_tuple = ('Hello', 'World', 'from', 'Python')
# output_string = concatenate_strings(input_tuple)
# print(output_string)  # Expected output: 'Hello World from Python'

input_tuple = ('Hello', 'World', 'from', 'Python')


def concatenate_strings(input_tuple):
    return ' '.join(input_tuple)


op = concatenate_strings( ('Hello', 'World', 'from', 'Python'))
print(op)

# Or

# output_string = ''
# for i in input_tuple:
#     if i == input_tuple[-1]:
#         output_string = output_string + i
#     else:
#         output_string = output_string + i + ' '
#
# print(output_string)

