#Replace multiple values
#Replace 20, 30, and 40 with 200, 300, and 400.
numbers = [10, 20, 30, 40, 50]
numbers[1:4] = [200, 300, 400]
print(numbers)

#Replace with fewer values
#Predict the output.
numbers = [1, 2, 3, 4, 5]
numbers[1:4] = [10]
print(numbers) #[1, 10, 5]


#Replace one with many
#Predict the output.
numbers = [1, 2, 3]
numbers[1:2] = [10, 20, 30]
print(numbers) #[1, 10, 20, 30, 3]

#Insert through slicing
#Insert 100 and 200 at index 2 without insert().
numbers[1:2] = [100, 200]
print(numbers)