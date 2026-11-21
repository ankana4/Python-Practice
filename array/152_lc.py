# 152. Maximum Product Subarray

#Brute-force appraoch
def maxProduct(nums):
    largest=nums[0]
    for i in range(0, len(nums)):
        data=1
        for j in range(i, len(nums)):
            data=data*nums[j]
            if data>largest:
                largest=data
    return largest

nums=[-2,0,-1]
# print(maxProduct(nums))      

#Optimal Approach
def maxProduct(nums):
    max_prod=nums[0]
    min_prod=nums[0]
    largest=nums[0]
    
    for i in range(1, len(nums)):
        curr=nums[i]
        a=curr
        b=curr*max_prod
        c=curr*min_prod
        
        max_prod=max(a, b, c)
        min_prod=min(a, b, c)
        largest=max(largest, max_prod)
    return largest

nums=[-2,0,-1]
print(maxProduct(nums))          