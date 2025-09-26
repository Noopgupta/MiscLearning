# Convert number to respective text. 11 should be double one, 1111 should be double one, double one.

num_dict = {0: 'Zero',
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'}

# n = str(input("Enter the number :"))
num = 455
n = list(str(num))
curr_num = 12
next_num = 13
num_text = []

print(num)
i = 0
for elem in n:
    if len(n) == 1:
        num_text.append(num_dict[int(n[i])])
        break
    elif i < len(n)-1:
        curr_num = n[i]
        next_num = n[i+1]
        if curr_num == next_num:
            num_text.append("double")
            num_text.append(num_dict[int(curr_num)])
            i += 2
        else:
            num_text.append(num_dict[int(curr_num)])
            i += 1
    elif i == len(n)-1:
        num_text.append(num_dict[int(n[i])])
        i += 1
    else:
        break

# print(n[-1], n[-2])
print(num_text)

text=''
for elem in range(len(num_text)):
    text = text + num_text[elem] + ' '

print(text)