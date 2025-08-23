nums = [1,3,5,6]
target = 7

for i in range(0, len(nums)):
    if nums[i] >= target:
        data = i
        break
    elif nums[i] < target:
        data = i+1
print(data)                      
         
       
       
       
nums = [1, 3, 4, 6]
target = 2
data = 0

for i in range(0, len(nums)):
    if nums[i] == target:
        data = i
    elif nums[i] < target:
        data = i+1
print(data)        
                         