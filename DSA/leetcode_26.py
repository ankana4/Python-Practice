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