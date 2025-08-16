list1 = [1,1,2]

temp_list = []
c = 0
for i in list1:
    if i not in temp_list: #[0,1,2,3]
        temp_list.append(i)
        c+=1
add_digit = len(list1) - len(temp_list)  
# print(add_digit)  
for j in range(0, add_digit): 
    temp_list.append(j)  

list1 = (temp_list)
print(c)
print(list1)  


#optimal approach

nums = [1, 2, 2]
        
i = 0
for j in range(1, len(nums)):
    if nums[j] != nums[i]:
        nums[i+1] = nums[j]
        i += 1
print(i+1)        