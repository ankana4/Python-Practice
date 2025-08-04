         
nums = [5,6,7]

int_data = 0

for i in range(0, len(nums)):
    int_data = int_data*10+nums[i]  
new_data = str(int_data+1)      
res = [int(j) for j in new_data]
print(res)    
     