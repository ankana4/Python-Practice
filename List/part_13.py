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