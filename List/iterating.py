#Direct iteration
#Print every element using a direct for loop.

numbers = [10, 20, 30, 40]
for i in numbers:
    print(i)
    

#Print every element and index using range(len(numbers)).    

numbers = [10, 20, 30, 40]
for i in range(len(numbers)):
    print(i, numbers[i])