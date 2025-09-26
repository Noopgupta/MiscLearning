
# Input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

# 0,0 -> 0,2  0,1 -> 1,2  0,2 -> 2,2
# 1,0 -> 0,1  1,1 -> 1,1  1,2 -> 2,1
# 2,0 -> 0,0  2,1 -> 1,0  2,2 -> 2,0

# row = 0 --> col = 2
# row = 1 --> col = 1
# row = 2 --> col = 0
#
# col = 0, row = 0
# col = 1, row = 1
# col = 2, row = 2


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# temp = 0
# for i in range(len(matrix)-1, -1, -1):
#     for j in range(len(matrix)):
#         temp = matrix[i][j]
#         matrix[i][j] = matrix[j][j]
#         matrix[j][j] = temp
#
# print(matrix)

# 0,0 -> 0,2  0,1 -> 1,2  0,2 -> 2,2
# 1,0 -> 0,1  1,1 -> 1,1  1,2 -> 2,1
# 2,0 -> 0,0  2,1 -> 1,0  2,2 -> 2,0
# def rotate(matrix):
#     n = len(matrix)
#
#     # Transpose the matrix
#     for i in range(n):  # Iterate over the rows
#         for j in range(i, n):  # Iterate over the columns starting from the current row 'i'
#             # Swap the elements at positions (i, j) and (j, i)
#             print(i, j)
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#             print(matrix)
#
#     # Reverse each row
#     for row in matrix:  # Iterate over each row in the matrix
#         row.reverse()  # Reverse the elements in the current row
#     print(matrix)
#
# rotate(matrix)


# matrix =
# [[1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9]]

# [1, 4, 7],
# [2, 5, 8],
# [3, 6, 9]

# [7, 4, 1],
# [8, 5, 2],
# [9, 6, 3]

def rotate(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j],  matrix[j][i] =  matrix[j][i],  matrix[i][j]
    print(matrix)

    for row in matrix:
        row.reverse()

rotate(matrix)
print(matrix)