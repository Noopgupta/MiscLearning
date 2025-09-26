#  796115110113721110141108 is the ascii values of pwd in reverse order.
#  Guess the pwd having only available keys in dictionary.

ascii_map = {
    65: 'A',
    66: 'B',
    67: 'C',
    68: 'D',
    69: 'E',
    70: 'F',
    71: 'G',
    72: 'H',
    73: 'I',
    74: 'J',
    75: 'K',
    76: 'L',
    77: 'M',
    78: 'N',
    79: 'O',
    80: 'P',
    81: 'Q',
    82: 'R',
    83: 'S',
    84: 'T',
    85: 'U',
    86: 'V',
    87: 'W',
    88: 'X',
    89: 'Y',
    90: 'Z',
    97: 'a',
    98: 'b',
    99: 'c',
    100: 'd',
    101: 'e',
    102: 'f',
    103: 'g',
    104: 'h',
    105: 'i',
    106: 'j',
    107: 'k',
    108: 'l',
    109: 'm',
    110: 'n',
    111: 'o',
    112: 'p',
    113: 'q',
    114: 'r',
    115: 's',
    116: 't',
    117: 'u',
    118: 'v',
    119: 'w',
    120: 'x',
    121: 'y',
    122: 'z',
    32: ' '
}

num = 796115110113721110141108
num_list = list(str(num))
rev_num = []


for j in range(len(num_list), 0, -1):
    rev_num.append(num_list[j-1])

print(rev_num)

text = ''
i = 0
chk_key = ''
for elem in rev_num:
    chk_key = int(str(chk_key) + rev_num[i])
    if chk_key in ascii_map:
        text = text + str(ascii_map.get(chk_key))
        i += 1
        chk_key = ''
    else:
        i += 1

print(text)



