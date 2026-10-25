#33. Search in Rotated Sorted Array
'''
Given an integer array nums, sorted in ascending order (with distinct values) and a target value k. 
The array is rotated at some pivot point that is unknown. 
Find the index at which k is present and if k is not present return -1.
'''


def rotatedArray(arr, x)->int:
    low=0
    high=len(arr)-1
    
    while low<=high:
        mid=(low+high)//2
        if arr[mid] == x:
            return mid
        if arr[low]<=arr[mid]:
            if arr[low]<=x and x<=arr[mid]:
                high=mid-1
            else:
                low=mid+1    
        elif arr[mid]<=x and x<=arr[high]:
            low=mid+1
        else:
            high=mid-1
    return -1
ra=rotatedArray([7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 6], 0)
print(ra)
                            

        
    