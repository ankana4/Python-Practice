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
