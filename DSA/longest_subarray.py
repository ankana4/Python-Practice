#Longest Subarray with given Sum K(Positives)

#Brute-force appraoch
nums = [10, 5, 2, 7, 1, 9]
k = 15  
n = len(nums)
l = 0
for i in range(0, n):
    s = 0
    for j in range(i, n):
        s += nums[j]
        if s==k:
            l=max(l, j-i+1)
print(l)                