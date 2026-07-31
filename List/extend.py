'''
Extend one list
Add all elements of b to a using extend().
a = [1, 2, 3]
b = [4, 5, 6]

'''

a = [1, 2, 3]
b = [4, 5, 6]

a.extend(b)
print(a)

#append() versus extend()
#Predict both outputs and explain the structural difference.
a = [1, 2]
a.append([3, 4])
print(a) #[1, 2, [3, 4]]

b = [1, 2]
b.extend([3, 4])
print(b) #[1, 2, 3, 4]


#Extend with a string
#Predict the output.
letters = ["a", "b"]
letters.extend("cd")
print(letters)  #["a", "b", "c", "d"]

#Extend with a tuple
#Predict the output and explain why it works.
numbers = [1, 2]
numbers.extend((3, 4))
print(numbers) #[1, 2, 3, 4]

#Extend with an integer
#What error occurs and why?
numbers = [1, 2]
numbers.extend(3)

#int is not iterable object.