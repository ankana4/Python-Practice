'''
Given an array of integers arr[], the task is to find the first equilibrium point in the array.

The equilibrium point in an array is an index (0-based indexing) such that the sum of all elements 
before that index is the same as the sum of elements after it. Return -1 if no such point exists. 

'''
#Brute-force approach
def findEquilibrium(arr):
    n=len(arr)
    for i in range(0, n):
        left_sum=0
        right_sum=0
        for j in range(0, i):
            left_sum+=arr[j]
            
        for j in range(i+1, n):
            right_sum+=arr[j]
        
        if left_sum == right_sum:
            return i
    return -1

arr=findEquilibrium([1, 1, 1, 1])
print(arr)           