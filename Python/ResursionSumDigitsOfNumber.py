# Find sum of digits for a number
# 10 = 1 + 0 = 1
# 10%10 = 1 and 0 remainder
# 112 >> 112%10 > 11 and 2 remainder >> 11%10 > 1 and 1 remainder

result = 0


def sum_digit(n) -> int:
    global result
    assert n >= 0 and int(n) == n
    if n < 10:
        result = result + n
    else:
        remainder = n % 10
        result = result + remainder
        sum_digit(n//10)

    return result


sum_digit = sum_digit(4)
print(sum_digit)


# number = 12
# digits = sum([int(digit) for digit in str(number)])
# print(digits)
