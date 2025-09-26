# 2^4 = 2*2*2*2=16


def calc_power(number, power) -> float:
    assert int(power) == power

    if power == 0:
        return 1
    elif power < 0:
        return 1 / calc_power(number, -power)
    else:
        return number * calc_power(number, power - 1)


# Example usage
result = calc_power(2, -2)
print(result)


# result = 1
# num_list = []
# def calc_power(number, power):
#     global result
#     num_list = [number] * power
#     for i in num_list:
#         result = result * i
#
#     print(result)
#
# calc_power(2,4)