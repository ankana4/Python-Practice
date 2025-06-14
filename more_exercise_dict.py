# Sorted dictionary by value
import operator
data = {'apple': 10, 'banana': 2, 'cherry': 5, 'date': 7}
ascending = dict(sorted(data.items(), key=operator.itemgetter(1)))
print(f'Ascending order by value {ascending}')


#add key to dictionary
data = {0:10, 1:20}
data[2] = 30
print(data)
  
  
#concatenate dictionary
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

new_data = {**dic1, **dic2, **dic3}
print(new_data)


#Write a Python script to check whether a given key already exists in a dictionary.
data = {0:10, 1:20, 4:22, 3:30, 4:40, 3:20}
for i in data.items():
    if i in data.keys():
        continue
print(data)    

#Write a Python program to iterate over dictionaries using for loops.
data = {0:10, 1:20, 4:22, 3:30}
for key, value in sorted(data.items()):
    print(f"{key} : {value}")


#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n = 5
dict_obj = {}
for i in range(1, n+1):
    dict_obj[f'{i}'] = i*i
print(dict_obj)


#Dictionary with Keys 1 to 15 and Their Squares
n = 15
dict_obj = {}
for i in range(1, n+1):
    dict_obj[i] = i*i
print(dict_obj)    


#Write a Python script to merge two Python dictionaries.
dict1 = {'a':'aa','b':'bb', 'c':'cc', 'd': 'dd'}
dict2 = {'p':'pp','e':'ee', 'f':'ff','g':'gg'}

dict1.update(dict2)
print(dict1)

#another approach
dict3 = {**dict1, **dict2}
print(dict3)

#Write a Python program to iterate over dictionaries using for loops.
dict1 = {'a':'aa','b':'bb', 'c':'cc', 'd': 'dd'}
dict2 = {'p':'pp','e':'ee', 'f':'ff','g':'gg'}
    
#Write a Python program to sum all the items in a dictionary.
dict_obj = {1:10, 2:13, 3:15, 4:18}
total_sum = 0
for key, val in dict_obj.items():
    total_sum = total_sum + val
print("Total sum is : ", total_sum)    
        
#Another approach
sum_of_items = sum(dict_obj.values())
print(sum_of_items)        

#Write a Python program to multiply all the items in a dictionary.
n = 5
dict_obj = {}
for i in range(1, n+1):
    dict_obj[i] = i*i*i
print(dict_obj)    

#Write a Python program to remove a key from a dictionary.
dict_obj = {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
dict_obj.pop(2)
print(dict_obj)

# #Write a Python program to map two lists into a dictionary.
list1 = [1, 2, 3, 4]
list2 = [2, 4, 5, 11]

dict_obj = dict(zip(list1, list2))
print(dict_obj)

#Write a Python program to sort a given dictionary by key.
color_dict = {
    'red': '#FF0000',
    'green': '#008000',
    'black': '#000000',
    'white': '#FFFFFF'
}
for key in sorted(color_dict):
    print(color_dict[key])
    
