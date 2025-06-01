fruit = ["apple", "banana", "guava"]
# print(fruit)

# Accessing items from list
access_fruit = fruit[1]
# print(access_fruit)

# Update item in list
# update_item = fruit[2]
# print(update_item)
# update_item = "Cherry"

# print(update_item)
fruit[2] = "cherry"
# print(fruit)

# Add item
fruit.append("kiwi")
# print(fruit)

# add list of new items 
# new_fruits = ["apple", "avogado", "mango"]
# fruit.append(new_fruits)
# print(fruit)

# Extend items 
extend_items = ["apple", "litchi", "mango"]
fruit.extend(extend_items)
# print(fruit)

# add another list of items
add_items = ["cucumber", "tomato"]
updated_list_of_items = fruit + add_items
# print(updated_lisew_item in new_items:
#     print_of_items)

# result = list((fruit, add_items, extend_items, []))
# print(result)

result = []
result.append(fruit)
result.append(["potato"])
result.append(add_items)
print(result)