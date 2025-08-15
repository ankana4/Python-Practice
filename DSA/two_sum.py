nums = [3, 2, 3]
target = 6
for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if(nums[i] + nums[j]) == target:
            print([i, j])  #Time complexity is o(n2)
            
            
# Two pointer approach
nums = [-3,-2,2,4,5,15,12,9]  #{-3:0, -2:1, 2:2, 4:3, 5:4, 15:5}
# nums = sorted(nums)
target = 14          

# first_index = 0
# last_index = len(nums)-1
# result = []

# while(first_index<last_index):
#     if nums[first_index] + nums[last_index] > target:
#         last_index -= 1
#     elif nums[first_index] + nums[last_index] < target:
#         first_index += 1   
#     else:
#         result = [first_index, last_index]   
#         break
# print(result)

temp_dict = {}
result = []
for i in range(0, len(nums)):
    current_num = nums[i]
    need = target - current_num
    if not need in temp_dict:
        temp_dict[current_num] = i
    else:
        result = [temp_dict[need], i]
        break
print(result)        
        
        
        
