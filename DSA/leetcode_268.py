nums1 = [0,1]
# nums = sorted(nums1) #[0,1,3]

# temp_list = []

# for i in range(0, len(nums)):
#     if i not in temp_list:
#         temp_list.append(i)#[0,1,2]
# digit = 0
# for j in range(0, len(temp_list)):
#     if nums[j] != temp_list[j]:
#         digit = j
# print(digit)   # Wrong approachhh

sum_of_indexes = 0
original_sum = 0

for i in range(0, len(nums1)):
    sum_of_indexes += i+1
    original_sum += nums1[i]

diff = sum_of_indexes - original_sum 
print(diff)   