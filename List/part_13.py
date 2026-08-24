#List multiplication
#Predict the output.
numbers = [1, 2]
print(numbers * 3) #[1, 2, 1, 2, 1, 2]

#List concatenation
#Predict the output.
a = [1, 2]
b = [3, 4]
print(a + b) #[1, 2, 3, 4]

#Nested multiplication trap
#Predict the output and explain why all rows change.
matrix = [[0] * 3] * 3
matrix[0][0] = 1
print(matrix) #[[1, 0, 0], [1, 0, 0], [1, 0, 0]]

#Correct nested-list creation
#Rewrite Question 103 so only the first row changes.
# Expected: [[1, 0, 0], [0, 0, 0], [0, 0, 0]]

#Mutation during iteration
#Does the loop terminate? Explain.
numbers = [1, 2, 3]
for number in numbers:
    numbers.append(number)
print(numbers)  #the loop keeps growing the list and effectively runs forever.


#Modify by index
#Predict the output.
numbers = [1, 2, 3, 4]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers) #[2, 4, 6, 8]