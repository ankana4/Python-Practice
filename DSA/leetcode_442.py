name = [4, 3, 2, 7, 8, 2, 3, 1]
# name = [1]

# temp_list = []
# for i in name:
#     if name.count(i) == 2 and i not in temp_list:
#         temp_list.append(i)   
# print(temp_list)            
        
temp_dict = {}
for i in name:
    if i in temp_dict:
        temp_dict[i] += 1
    else:
        temp_dict[i] = 1
result = []
for k, v in temp_dict.items():
    if v == 2:
        result.append(k)
print(result) 