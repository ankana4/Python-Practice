'''
Given an array of integers arr[], the task is to find the first equilibrium point in the array.

The equilibrium point in an array is an index (0-based indexing) such that the sum of all elements 
before that index is the same as the sum of elements after it. 
Return -1 if no such point exists.
'''
#Brute-force approach

def equilibriumPoint(arr):
    n=len(arr)
    for i in range(0, n):
        leftSum=0
        rightSum=0
        for j in range(0, i):
            leftSum+=arr[j]
        for j in range(i+1, n):
            rightSum+=arr[j]
         
        if leftSum == rightSum:
            return i
    return -1

arr=[-7, 1, 5, 2, -4, 3, 0]
eq=equilibriumPoint(arr)  
print(eq)          


#Better approach
def equilibrium_point(arr):
    n=len(arr)
    totalSum=sum(arr)
    leftSum=0
    for i in range(0, n):
        rightSum=totalSum-leftSum-arr[i]
        
        if rightSum == leftSum:
            return i
        
        leftSum+=arr[i]
    return -1

arr=[1, 2, 0, 3]
print(equilibrium_point(arr))    