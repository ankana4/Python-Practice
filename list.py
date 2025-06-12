'''
List - It is a build-in data structure and sequence type object in python.
- The items in list are in ordered way.
- List can be mutable(we can add, update or remove items).
- List can store any type of data(string, integers, list etc.) in single variable.
- It can contain duplicate data also.

'''
'Examples of List are :- '

fruit = ["apple", "banana", "guava"]
print(fruit)

# Accessing items from list
access_fruit = fruit[1]
print(access_fruit)

# Update item in list
update_item = fruit[2]
print(update_item)
update_item = "Cherry"

# print(update_item)
fruit[2] = "cherry"
print(fruit)

# Add item
fruit.append("kiwi")
print(fruit)

# add list of new items 
new_fruits = ["apple", "avogado", "mango"]
fruit.append(new_fruits)
print(fruit)

# Extend items 
extend_items = ["litchi", "mango"]
fruit.extend(extend_items)
extend_more_items = "chilli"
fruit.extend(extend_more_items)
print(fruit)

# add another list of items
add_items = ["cucumber", "tomato"]
updated_list_of_items = fruit + add_items
result = list((fruit, add_items, extend_items, []))
print(result)

result = []
result.append(fruit)
result.append(["potato"])
result.append(add_items)
# print(result)

# Remove items
fruit.remove("apple")
print(fruit)

fruit.pop(3)
fruit.reverse()
print(fruit)


#remove data from list
list = [0,2,3,4,5,6,7]
for i in list: #i=3  list=[2,4,6]
    list.remove(i) 
print(list)


#List unpacking examples
list1 = ['a']
list2 = ['b', 'c']
list3 = ['d', 'e']

new_list = [*list1, *list2, *list3]
print(new_list)

#Add elements in between
a = [1, 2]
b = [4, 5]
new_list = [*a, 3, *b, 6]
print(new_list)

#Clone(copy) a list
original = ['x', 'y', 'z']
copy = [*original]
print(copy)

#Unpack inside a function argument
def show_names(a, b, c):
    print(a, b, c)
    
names = ['Arun', 'Barun', 'Nitai']
show_names(*names) 

#Nested unpacking
nested = [[1, 2], [3, 4]]
flat = [*nested[0], *nested[1]]
print(flat)