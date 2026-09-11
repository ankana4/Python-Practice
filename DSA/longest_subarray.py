#Longest Subarray with given Sum K(Positives)

#Brute-force appraoch
nums = [10, 5, 2, 7, 1, 9]
k = 15  
n = len(nums)
l = 0
for i in range(0, n):
    for j in range(i, n):
        s = 0
        for x in range(i, j+1):
            s += nums[x]
        if s==k:
            l=max(l, j-i+1)
print(l)                


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


#Bettter approach
n = len(nums)
pre_sum_dict={}
sum_so_far = 0
max_len = 0

for i in range(0, n):
    sum_so_far += nums[i]
    if sum_so_far == k:
        max_len = i+1
    rem = sum_so_far - k
    if rem in pre_sum_dict:
        length = i-pre_sum_dict[rem]
        max_len = max(max_len, length)
    if sum_so_far not in pre_sum_dict:
        pre_sum_dict[sum_so_far] = i        
print(max_len)        