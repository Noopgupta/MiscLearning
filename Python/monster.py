grp = 'PPPPPP@PPP@PP$PP'
substrings1 = grp.split('@') + grp.split('$')
count1 = []
for elem in substrings1:
    count1.append(len(elem))

print(min(count1))
