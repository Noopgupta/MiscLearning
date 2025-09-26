# profit = [60, 100, 120, 800, 45]
# weight = [40, 20, 10, 30, 50]
# target_sum = 50


result = []

def find_subarrays_with_sum(weight, target_sum):

    current_sum = 0
    start = 0
    diff = 0
    l = len(weight)

    for end in range(l):
        current_sum += weight[end]


        while current_sum > target_sum and start <= end:
            diff = current_sum - target_sum
            if diff in weight:
                result.append(weight[start:end + 1])
                for sublist in result:
                    for element in sublist:
                        if element == diff:
                            sublist.remove(element)
                            current_sum = 0
                            for elem in sublist:
                                weight.remove(elem)

                            find_subarrays_with_sum(weight, target_sum)

            else:
                current_sum -= weight[start]
                start += 1

        if current_sum == target_sum:
            result.append(weight[start:end + 1])
            for sublist in result:
                for elem in sublist:
                    weight.remove(elem)



            find_subarrays_with_sum(weight, target_sum)

    return result


weight_list = [40, 20, 10, 30, 50]
# weight_list = [50]
weight = sorted(weight_list)
target_sum = 50
subarrays = find_subarrays_with_sum(weight, target_sum)
print(subarrays)



result = [[10,40],[20,30],[50]]