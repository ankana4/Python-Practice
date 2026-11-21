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
print(maxProduct(nums))            