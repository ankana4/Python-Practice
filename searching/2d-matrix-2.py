'''
Given a 2D array matrix where each row is sorted in ascending order from left to right and each column is sorted in ascending order from top to bottom, 
write an efficient algorithm to search for a specific integer target in the matrix.

LC-240
'''
#brute-force approach
def searchMatrix(matrix, target):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j]==target:
                return [i, j]
    return [-1, -1]
matrix=[
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
sm=searchMatrix(matrix, 6)
print(sm)
        