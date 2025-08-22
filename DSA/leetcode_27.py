nums = [0,1,2,2,3,0,4,2]
val = 2
temp_list = []
c=0
for i in nums:
    if i != val:
        temp_list.append(i)
        c+=1
        
    else:
        continue        
add_digit = len(nums) - len(temp_list)

for j in range(0, add_digit):
    temp_list.append(j)

nums[:] = temp_list
print(nums)  
print(c)           
    

#Optimize approach        
nums = [0,1,2,2,3,0,4,2]
val = 2       

j = 0
for i in range(1, len(nums)):
    if nums[i] != val:
        nums[j] = nums[i]
        j += 1
print(j)            