# #!/bin/python
#
# import math
# import os
# import random
# import re
# import sys


#
# Complete the 'playSegments' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY coins as parameter.
#
coins = []
def playSegments(coins):
    # Write your code here
    # [1,1,1,0,1]

    player1_score = 0
    player2_score = 0
    play_times = 0
    coins_len = len(coins)

    for play_times in range(coins_len):
        player1_score = 0
        player2_score = 0
        for i in range(coins_len):
            if play_times == 0:
                player1_score = 0
                if coins[i] == 1:
                    player2_score += 1
                else:
                    player2_score -= 1


# 1, 0-4
            if play_times > 0:
                if i < play_times:
                    if coins[i] == 1:
                        player1_score += 1
                    else:
                        player1_score -= 1
                else:
                    if coins[i] == 1:
                        player2_score += 1
                    else:
                        player2_score -= 1

        if player1_score > player2_score:
            return play_times
            break

# coins = []
#
# def playSegments(coins):
#     list_length = len(coins)
#     print(list_length)
#     for i in range(list_length):
#         if coins[i] == 0:
#             coins[i] = -1
#
#     print(coins)
#
#     total_score = sum(coins)
#     print("total_score" + str(total_score))
#
#     player1_score = 0
#     play_times = 0
#     for i in range(list_length):
#         if play_times == 0:
#             player1_score = 0
#             player2_score = total_score - player1_score
#             if player1_score > player2_score:
#                 return play_times
#                 break
#             else:
#                 play_times += 1
#                 player1_score = 0
#                 player2_score = 0
#
#         if play_times > 0:
#             player1_score += coins[i]
#             player2_score = total_score - player1_score
#             if player1_score > player2_score:
#                 return play_times
#                 break
#             else:
#                 play_times += 1
#



if __name__ == '__main__':
    # value = playSegments([1, 1, 1, 0, 1])
    # value = playSegments([1, 0, 0, 1, 0])
    # value = playSegments([1, 0, 1, 0, 1])
    # value = playSegments([0, 0, 0, 0, 1])
    value = playSegments([1, 1, 1, 1, 1])
    print("Play_times" + str(value))


