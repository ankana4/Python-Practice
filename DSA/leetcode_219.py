nums = [1,2,3,1]
k = 3
temp_dict = {}

for i in range(0, len(nums)):
    if nums[i] not in temp_dict:
        temp_dict[nums[i]] = i
    else:
        old_index = temp_dict[nums[i]]   
        if abs(old_index - i) <=k:
            print("True")
        else:
            temp_dict[nums[i]] = i    
print("False")            
        