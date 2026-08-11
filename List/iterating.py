#Direct iteration
#Print every element using a direct for loop.

numbers = [10, 20, 30, 40]
for i in numbers:
    print(i)
    

#Print every element and index using range(len(numbers)).    

numbers = [10, 20, 30, 40]
for i in range(len(numbers)):
    print(i, numbers[i])
    

#Print output in the form "Index 0: 10".
numbers = [10, 20, 30]    

for i, n in enumerate(numbers):
    print(f"Index {i} : {n}")
    

#Print elements in reverse order without reverse() or slicing.    

numbers = [10, 20, 30, 40]
for i in range(len(numbers)-1, -1, -1):
    print(numbers[i])