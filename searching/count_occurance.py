'''
765. Find out how many times the array is rotated
Given an integer array nums of size n, sorted in ascending order with distinct values. 
The array has been right rotated an unknown number of times, between 0 and n-1 (including). 
Determine the number of rotations performed on the array.
'''
def countOccurance(arr):
    low=0
    high=len(arr)-1
    ans=float('inf')
    index=-1
    while low<=high:
        mid=(low+high)//2
        if arr[low]==arr[mid]==arr[high]:
            if arr[low]<ans:
                index=low
                ans=arr[low]
            low+=1
            high-=1
            continue
        if arr[low]<=arr[mid]:
            if arr[low]<ans:
                index=low
                ans=arr[low]
            low=mid+1
        else:
            high=mid-1
            if arr[mid]<ans:
                index=mid
                ans=arr[mid]
    return index
coo=countOccurance([4, 5, 6, 7, 0, 1, 2, 3])
print(coo)        
                        