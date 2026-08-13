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

