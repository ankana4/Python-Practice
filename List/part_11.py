#Aliasing
#Predict the output and explain why both names show the change.
a = [1, 2, 3]
b = a
b.append(4) #a=[1, 2, 3, 4]
print(a) #[1, 2, 3, 4]
print(b)  #[1, 2, 3, 4]

#Independent copy
#Correct Question above using copy().

a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a) #[1, 2, 3]
print(b) #[1, 2, 3, 4]


#Independent copy by slicing
#Create the same copy using [:].
a = [1, 2, 3]
b = a[:]
b.append(4)
print(a) #[1, 2, 3]
print(b) #[1, 2, 3, 4]


#Predict both Boolean outputs.
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) #True, check values are equal
print(a is b) #False, check if they are the same object


#Predict the output and explain why an inner change appears in both.
a = [[1, 2], [3, 4]]
b = a.copy()
b[0].append(99)
print(a) #[[1, 2, 99], [3, 4]]
print(b) #[[1, 2, 99], [3, 4]]