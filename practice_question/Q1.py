#Count Numbers
numbers = [10, 20, 30, 10, 20, 10]
temp_dict = {}

for num in numbers:
    if num in temp_dict:
        temp_dict[num]+=1
    else:
        temp_dict[num]=1
print(temp_dict)            