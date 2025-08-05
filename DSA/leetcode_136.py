nums = [1]
data = 0
for i in nums:
    if nums.count(i) < 2:
        data = i
print(data)  