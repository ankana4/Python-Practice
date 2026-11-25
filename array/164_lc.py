#164. Maximum Gap

#Brute-force approach
def maxGap(nums):
    n=len(nums)
    if nums is None or n<2:
        return 0
    nums=sorted(nums)
    maxG=nums[1]-nums[0]
    
    for i in range(2, n):
        maxG=max(maxG, nums[i]-nums[i-1])
    return maxG

nums=[3, 6, 9, 1]
print(maxGap(nums))    