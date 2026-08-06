#First three elements
#Extract the first three elements.
numbers = [10, 20, 30, 40, 50, 60]
print(numbers[:3])


#Last three elements
#Extract the last three elements.
print(numbers[-3:])

#Index 1 to 4
#Extract elements from index 1 through index 4, inclusive
print(numbers[1:5])

#Every second element
#Extract every second element.
print(numbers[1::2])

#Odd indexes
#Extract elements at odd indexes.
print(numbers[1::2])

#Reverse with slicing
#Reverse the list using slicing.
print(numbers[::-1])

#Copy with slicing
#Create an independent shallow copy using [:].
numbers = [10, 20, 30, 40, 50, 60]
new_list = numbers[:]
print(new_list)

#Omitted slice indexes
#Explain numbers[:4] - [10, 20, 30, 40]
# numbers[2:]- [30, 40, 50, 60]
# numbers[:] - [10, 20, 30, 40, 50, 60]
# numbers[::2] - [10, 30, 50]
# and numbers[::-1] - [60, 50, 40, 30, 20, 10]

#Slice beyond length
#Predict the output and explain why no error occurs.
numbers = [1, 2, 3]
print(numbers[0:100]) #No error occurs because Python slicing safely adjusts an out-of-range stop index to the list’s actual length.

#Indexing versus slicing
#Compare numbers[100] with numbers[100:200]. Which raises an error, and why?
#The difference is that indexing accesses a single element, while slicing returns a portion of the list.
'''
numbers = [1, 2, 3]
print(numbers[100]) #IndexError: list index out of range
print(numbers[100:200]) #[]
'''