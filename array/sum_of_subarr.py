# Given an array arr[], find the sum of all the subarrays of the given array.

#Brute-force approach

def sumOfSubarr(arr):
    n=len(arr)
    total=0
    for i in range(0, n):
        for j in range(i, n):
            for k in range(i, j+1):
                total+=arr[k]
    return total

arr=[1, 2, 3]
print(sumOfSubarr(arr))            \
    
#better approach

def sumOfSubarr(arr):
    total=0
    n=len(arr)
    
    for i in range(0,n):
        current_sum=0
        for j in range(i, n):
            current_sum+=arr[j]
            total+=current_sum
    return total

arr=[1, 3]
print(sumOfSubarr(arr))           


#Optimal approach
def sumOfSubarr(arr):
    n=len(arr)
    total=0
    for i in range(0, n):
        total+=arr[i]*(i+1)*(n-i)
    return total

arr=[1, 2, 3, 4]
print(sumOfSubarr(arr))    