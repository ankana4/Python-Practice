'''
Given a 2-D array mat where the elements of each row are sorted in non-decreasing order, 
and the first element of a row is greater than the last element of the previous row (if it exists), 
and an integer target, determine if the target exists in the given mat or not.
LC-74

'''
#using Brute-force approach
def searchMatrix(matrix, target):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j]==target:
                return True
    return False        

matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
sm=searchMatrix(matrix, 17)
print(sm)

def binarySearch(arr, target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif target<arr[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1            

def searchMatrix(matrix, target):
    for i in range(0, len(matrix)):
        if matrix[i][0]<=target and target<=matrix[i][-1]:
            return binarySearch(matrix[i], target) !=-1
    return False    

matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
sm1=searchMatrix(matrix, 60)
print(sm1)