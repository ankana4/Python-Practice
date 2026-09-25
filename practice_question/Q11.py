#Find duplicate values
numbers = [10, 20, 10, 30, 20, 40, 10]
num_dict = {}

for num in numbers:
    if num in num_dict:
        num_dict[num] +=1
    else:
        num_dict[num] = 1
data = []
for k, v in num_dict.items():
    if v>1:
        data.append(k)
print(data)                    