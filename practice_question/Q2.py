#Count characters
word = "banana"
temp_dict = {}

for i in word:
    if i in temp_dict:
        temp_dict[i]+=1
    else:
        temp_dict[i]=1
print(temp_dict)            