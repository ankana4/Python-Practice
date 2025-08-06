nums = [0,1,0,3,12]

temp_list = []
for i in range(0, len(nums)):
    if nums[i] != 0:
        temp_list.append(nums[i])  #[1, 3, 12]
    
avg_len = len(nums) - len(temp_list) #2
for j in range(0, avg_len):
    temp_list.append(0)
nums[:] = temp_list
print(nums) 