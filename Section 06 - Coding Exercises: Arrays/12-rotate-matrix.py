# Rotate Matrix/ Image - LeetCode 48
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.

# DO NOT allocate another 2D matrix and do the rotation.

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

def rotate(matrix):
    # Matrix Transpose
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    for row in matrix:
        row.reverse()


def print_matrix(matrix):
    for row in matrix:
        print(row)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_matrix(matrix)
rotate(matrix)
print(f"Rotated Matrix:")
print_matrix(matrix)
