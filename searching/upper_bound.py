'''
Given a sorted array of nums and an integer x, write a program to find the upper bound of x.

The upper bound of x is defined as the smallest index i such that nums[i] > x.

If no such index is found, return the size of the array.

'''
def upperBound(arr, x):
    ans=len(arr)
    low=0
    high=len(arr)-1
    
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]>x:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans           

ub = print(upperBound([2, 3, 6, 7, 8, 8, 11, 11, 11], 12))
