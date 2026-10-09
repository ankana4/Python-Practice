'''
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value. 
If the target is not found in the array, return [-1, -1].
'''
def firstOccurance(arr, x):
    first = -1
    low=0
    high=len(arr)-1
    
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]>=x:
            first=mid
            high=mid-1
        else:
            low=mid+1
    if first == -1 or arr[first] != x:
        return -1       
    return first            
    
def lastOccurance(arr, x):
    last = -1
    low=0
    high = len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if arr[mid]<=x:
            last=mid
            low=mid+1
        else:
            high=mid-1
    if last == -1 or arr[last] != x:
                return -1      
    return last
                
fo=firstOccurance([5, 7, 7, 8, 8, 10], 8)
lo=lastOccurance([5, 7, 7, 8, 8, 10], 8)
print(fo)    
print(lo)