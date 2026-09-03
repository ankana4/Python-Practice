#Remove Duplicates in-place from Sorted Array
#Brute-force approach

nums = [1,1,2,2,2,3,3]
output = []

for i in nums:
    if i not in output:
        output.append(i)
add_digit = len(nums) - len(output)
for j in range(0, add_digit):
    output.append(0)
nums = output    
print(output)            


#Another brute force approach
seen = set()
index = 0
for i in nums:
    if i not in seen:
        seen.add(i)
        nums[index] = i
        index += 1
print(index)        
print(nums)