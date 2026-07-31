#Insert at a position
#Insert 20 between 10 and 30.
numbers = [10, 30, 40]
numbers.insert(1, 20)
print(numbers)

numbers = [10, 20, 60, 50, 20]
numbers.insert(2, 50)
print(numbers)

#Insert at the beginning
#Insert 5 at index 0.
numbers = [10, 20, 30]
numbers.insert(0, 5)
print(numbers)


#Insert at the end
#Use insert(), not append(), to add 40 at the end.
numbers = [10, 20, 30]
numbers.insert(len(numbers), 40)
print(numbers)

#Negative insert index
#Predict the result.
numbers = [10, 20, 30, 40]
numbers.insert(-1, 99)
print(numbers) #[10, 20, 30, 99, 40]

#Index larger than length
#Predict the output.
numbers = [1, 2, 3]
numbers.insert(100, 4)
print(numbers) #[1, 2, 3, 4]

#Very small negative index
#Predict the output.
numbers = [1, 2, 3]
numbers.insert(-100, 0)
print(numbers) #[0, 1, 2, 3]