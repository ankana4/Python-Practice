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