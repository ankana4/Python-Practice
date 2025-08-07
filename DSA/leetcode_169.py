nums = [2,2,1,1,1,2,2]
# size = len(nums)
# c = 0
# for i in nums:
#     if nums.count(i) > size/2:
#         c = i
# print(c)                       
          
temp_dict = {}
size = len(nums)
for i in nums:
    if i in temp_dict:
        temp_dict[i] += 1
    else:
        temp_dict[i] = 1

for k, v in temp_dict.items():
    if v > size/2:
        print(k)                            
