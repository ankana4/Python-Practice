
nums = [1,1,1, 0, 1, 1]

c = 0
ans = 0
for i in range(0, len(nums)):
    if nums[i] == 1:
        c += 1
    else:
        c = 0
    
    ans = max(ans, c)
print(ans)         