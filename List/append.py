# Append one element
#Add 40 to the end of the list using append().
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)

#Append user input
#Take a number from the user and append it to an existing list.
number = int(input("Enter a number: "))
numbers.append(number)
print(numbers)

#Append values using a loop
#Start with an empty list and append numbers from 1 to 10.
# Expected: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
empty_list = []
for i in range(1, 11):
    empty_list.append(i)
print(empty_list)

#Append only even numbers
#Create a list containing all even numbers from 1 to 20.
even_data = []
for i in range(1, 20):
    if i%2 == 0:
        even_data.append(i)
print(even_data)        

#10. Append squares
#Create [1, 4, 9, 16, 25] using a loop and append()
square_data = []
for i in range(1, 6):
    square_data.append(i*i)
print(square_data)    

#Predict the output and explain why [4, 5] becomes one nested element.
a = [1, 2, 3]
a.append([4, 5])
print(a) #[1, 2, 3, [4, 5]]

#Predict both outputs and explain why result is None.
numbers = [1, 2, 3]
result = numbers.append(4)
print(numbers)  #[1, 2, 3, 4]
print(result) #None


a = [1, 2, 3]
b = a
b.append(4) 
print(a) #[1, 2,3, 4]
print(b) #[1, 2, 3, 4]