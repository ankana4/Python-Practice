'''
Given an array arr[] of size n - 1 containing distinct integers in the range [1, n]. 
The array represents a permutation of the integers from 1 to n with exactly one element missing.

Find and return the missing element.
'''

#Brute-force approach
def missingNum(arr: list[int]) -> int:
    
    for i in range(1, len(arr)+2):
        flag=False
        for j in range(len(arr)):
            if arr[j]==i:
                flag=True
                break
        
        if flag==False:
            return i
                    
arr=[1]
print(missingNum(arr))                    