import copy
x = [1]
x.append(x)  
print(x)


x = []
x.append(x)
print(x)


data = []
for i in range(3):
    temp = []           
    temp.append(i * 2)  
    data.append(temp)  
print(data)


data = []
temp = [] 

for i in range(3): #i=4
	temp.append(i*2) #temp[0,2,4]
	data.append(copy.deepcopy(temp)) #[[0],[0,2],[0,2,4]]
print(data)

#remove data from list
list = [0,2,3,4,5,6,7]
for i in list: #i=3  list=[2,4,6]
    list.remove(i) 
print(list)
