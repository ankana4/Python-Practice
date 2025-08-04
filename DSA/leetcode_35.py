nums = [1,3,5,6]
target = 7

for i in range(0, len(nums)):
    if nums[i] >= target:
        data = i
        break
    elif nums[i] < target:
        data = i+1
print(data)                      
         