'''
Given an array nums sorted in non-decreasing order. 
Every number in the array except one appears twice. Find the single number in the array.
'''

#Brute-force approach - TC:0(n)
def singleNonDuplicate(arr):
    n=len(arr)
    for i in range(1, n):
        if n==1:
            return arr[0]
        if i==0:
            if arr[i]!=arr[i+1]:
                return arr[0]
        elif i == n-1:
            if arr[i]!=arr[i-1]:
                return arr[i]
        elif arr[i]!=arr[i+1] and arr[i]!=arr[i-1]:
            return arr[i]
sA=singleNonDuplicate([1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 6])
print(sA)        

#By using binary search algorithm
def singleNonDuplicate(arr):
    n=len(arr)
    if n==1:
        return arr[0]
    if arr[0]!=arr[1]:
        return arr[0]
    if arr[n-1]!=arr[n-2]:
        return arr[n-1]
    low=1
    high=n-2
    while low<=high:
        mid=(low+high)//2
        if arr[mid]!=arr[mid+1] and arr[mid]!=arr[mid-1]:
            return arr[mid]
        if ((mid%2==1 and arr[mid-1]==arr[mid])or (mid%2==0 and arr[mid+1]==arr[mid])):
            low=mid+1
        else:
            high=mid-1
    return -1
sND=singleNonDuplicate([2, 2, 3])
print(sND)            