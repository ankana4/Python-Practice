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
        
        
#better approach using binary search
def binarySearch(arr, target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1

def searchMatrix(matrix, target):
    for i in range(0, len(matrix)):
        index=binarySearch(matrix[i], target)
        if index!=-1:
            return[i, index]
    return [-1, -1]
smatrix=searchMatrix(matrix, 15)
print(smatrix)

#optimized approach
def optimizeSearchMatrix(matrix, target):
    n=len(matrix)
    m=len(matrix[0])
    row=0
    col=m-1
    while row<=n and col>=0:
        if matrix[row][col]==target:
            return True
        elif matrix[row][col]<target:
            row+=1
        else:
            col-=1
    return False            
osmatrix=optimizeSearchMatrix(matrix, 9)
print(osmatrix)