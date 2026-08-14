#Sum without sum()
#Find the total using a loop.
numbers = [10, 20, 30, 40]
sum = 0
for i in numbers:
    sum = sum+i
print(sum)    

#Largest without max()
#Find the largest value using a loop.
largest = numbers[0]
for i in numbers:
    if i>largest:
        largest=i
print(largest)        


#Smallest without min()
#Find the smallest value using a loop.
smallest=numbers[0]
for i in numbers:
    if i< smallest:
        smallest=i
print(smallest)

#Second-largest distinct value
#Return 30.
numbers = [10, 40, 20, 40, 30]
largest = numbers[0]
second_largest = None

for i in numbers:
    if i>largest:
        second_largest=largest
        largest=i
    elif i<largest:
        if second_largest is None or i>second_largest:
            second_largest=i
print(second_largest)    

#Remove duplicates preserving order
#Return [1, 2, 3, 4] without set().
numbers = [1, 2, 1, 3, 2, 4, 1]

new_list = []
for i in numbers:
    if i not in new_list:
        new_list.append(i)
print(new_list)


#Separate even and odd
#Build two lists: even_numbers and odd_numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = []
odd_numbers = []

for i in numbers:
    if i%2==0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)
print(even_numbers)
print(odd_numbers)

#Build separate lists for positive and negative values.
numbers = [1, -2, -4, 7, 8, -5]
positive = []
negative = []
for i in numbers:
    if i>0:
        positive.append(i)
    else:
        negative.append(i)
print(positive)
print(negative)