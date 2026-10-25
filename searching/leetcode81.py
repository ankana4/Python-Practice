'''
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible.
'''

def rotatedArr2(arr, n):
    low = 0
    high = len(arr)-1
    
    while low<=high:
        mid=(low+high)//2
        if arr[mid] == n:
            return True
        if arr[low]==arr[mid] and arr[mid]==arr[high]:
            low+=1
            high-=1
            continue
        if arr[low]<=arr[mid]:
            if arr[low]<=n and n<=arr[mid]:
                high=mid-1
            else:
                low=mid+1
        elif arr[mid]<=n and n <=arr[high]:
            low=mid+1
        else:
            high=mid-1
    return False

rA=rotatedArr2([3, 3, 3, 6, 1, 2, 3, 3], 1)
print(rA)                         
    