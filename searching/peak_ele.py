'''
A peak element is an element that is strictly greater than its neighbors. Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may assume that an element is always considered to be strictly greater than a neighbor that is outside the array boundary (nums[-1] = nums[n] = -INF).

'''
#Brute-force approach -TC - 0(n)
def findPeak(arr):
    for i in range(0, len(arr)):
        if ((i==0 or arr[i-1]<arr[i]) and (i==len(arr)-1 or arr[i]>arr[i+1])):
            return i
fp=findPeak([1, 2, 1, 3, 5, 6, 4])
print(fp)        