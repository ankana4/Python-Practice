#remove() a value
#Remove 30 from the list.
numbers = [10, 20, 30, 40] #Remove the number
numbers.remove(20)
print(numbers) #[10, 30, 40]

#remove() first occurrence
#Predict the output.
numbers = [10, 20, 10, 30, 10]
numbers.remove(10)
print(numbers) #[20, 10, 30, 10]

#Remove all occurrences
#Remove every 10.
numbers = [10, 20, 10, 30, 10, 40]
# Expected: [20, 30, 40]
for i in numbers:
    if i == 10:
        numbers.remove(i) 
print(numbers)        


numbers = [i for i in numbers if i != 10]
print(numbers)

#Remove all in place
#Modifying the original list without creating a final replacement list.

numbers[:] = [i for i in numbers if i != 10]
print(numbers)


#Removing while iterating
#Predict the output and explain why some values may remain.
numbers = [1, 2, 2, 2, 3]
for number in numbers:
    if number == 2:
        numbers.remove(number) #[1,2,3]
print(numbers) 

#Safe repeated removal
#So every 2 is removed safely.
numbers[:] = [number for number in numbers if number!=2]
print(numbers)

#Remove only if present
#Remove 50 only when it exists; your code must not raise an error.
numbers = [10, 20, 30, 40]
for i in numbers:
    if i == 50:
        numbers.remove(i)
    else:
        break
print(numbers)    

#Missing value
#What happens when remove() cannot find the value?
numbers = [10, 20, 30]
# numbers.remove(100) #100 not in list

#pop() last element
#Remove the last element using pop().
numbers = [10, 20, 30, 40]
numbers.pop()
print(numbers)

#Store popped value
#Print both the updated list and the removed value.
numbers = [100, 200, 300, 400]
removed_numbers = numbers.pop()
print(numbers)
print(removed_numbers)

#Pop at an index
#Remove the element at index 1.
numbers = [23, 24, 25, 26, 27]
deleted_numbers = numbers.pop(1)
print(numbers)
print(deleted_numbers)


#pop() without argument
#Predict both outputs.
numbers = [10, 20, 30]
value = numbers.pop()
# print(numbers) #[10, 20]
# print(value) #30


#Invalid pop index
#What error occurs?
numbers = [10, 20, 30]
# numbers.pop(10)  #pop index out of range

#Pop from empty list
#What error occurs?
numbers = []
# numbers.pop()  #pop from empty list
# print(numbers)

#List as stack
#Push 10, 20, and 30 with append(), then pop one value.
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)
stack.pop()
print(stack)


#del by index
#Delete the element at index 2.
numbers = [10, 20, 30, 40]
del numbers[2]
print(numbers)

#del a range
#Delete 20, 30, and 40 using slicing with del.
numbers = [10, 20, 30, 40, 50, 60]
del numbers[1:4]
print(numbers)

#Delete odd-indexed elements
#Delete the elements at indexes 1, 3, 5, and 7.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# Expected: [1, 3, 5, 7]
del numbers[1::1]
print(numbers)        


#Delete the variable
#Predict what happens and explain deletion versus emptying.
numbers = [1, 2, 3]
del numbers
# print(numbers) #numbers is not defined

#clear() all elements
#Empty the list using clear().
numbers = [10, 20, 30]
numbers.clear()
print(numbers)

#clear() versus del
#Explain the difference between numbers.clear() and del numbers.
''' 
clear() - removes all elements
del - deletes the variable
del - delete one variable from element
del - delete multiple elements from list
del - removes all element 

'''

#Shared reference with clear()
#Predict both outputs and explain them.
a = [1, 2, 3]
b = a
a.clear()
print(a) #[]
print(b) #[]


#Reassignment versus clear()
#Predict both outputs and explain why this differs from clear().
a = [1, 2, 3]  
b = a
a = []
print(a) #[]
print(b) #[1, 2, 3]