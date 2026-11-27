#15. 3Sum

#Brute-force approach
def threeSum(nums):
    n=len(nums)
    result=set()
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if nums[i]+nums[j]+nums[k]==0:
                    triplet=sorted([nums[i], nums[j], nums[k]])
                    result.add(tuple(triplet))
                    
    return [list(t) for t in result]                


nums=[-1,0,1,2,-1,-4]
# print(threeSum(nums))

#Better approach
def threeSum(nums):
    n=len(nums)
    result=set()
    
    for i in range(n):
        seen=set()
        
        for j in range(i+1, n):
            third=-(nums[i]+nums[j])
            if third in seen:
                triplet=sorted([nums[i], nums[j], third])
                result.add(tuple(triplet))
            seen.add(nums[j])
    return [list(t) for t in result]
nums=[-1,0,1,2,-1,-4]
print(threeSum(nums))           