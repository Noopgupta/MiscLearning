# reverse the string before i, remove i and then keep the rest as it is
# I/P string >> O/P rtsng

str = "stringstring"
op_str = []
str_list = list(str)

# print(str_list[])
c = 0
l = len(str_list)
while c in range(0, l):
    if str_list[c] == 'i':
        op_str.reverse()
        c = c + 1
    op_str.append(str_list[c])
    str_list = str_list[c+1:]

    print(c, str_list, op_str)