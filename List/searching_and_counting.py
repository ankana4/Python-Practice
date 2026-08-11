#First occurrence
#Find the index of the first 7.
numbers = [4, 7, 2, 7, 9]
for i in range(len(numbers)):
    if numbers[i] == 7:
        print(i)
        break
    

#Last occurrence
#Find the index of the last 7 without using a reverse-index shortcut.    
for i in range(len(numbers)-1, -1, -1):
    if numbers[i] == 7:
        print(i)
        break
    
#All occurrence indexes
#Return [1, 3, 5].
numbers = [4, 7, 2, 7, 9, 7]   
for i in range(len(numbers)):
    if numbers[i] == 7:
        print(i)
        

#Count positive, negative, zero
#Count each category separately.
numbers = [4, -2, 0, 7, -5, 0, 8]    
positive = 0
negative = 0
zero = 0

for i in numbers:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
    else:
        zero += 1
print(positive, negative, zero)        


#Count even and odd
#Count even and odd values separately.
even_count = 0
odd_count = 0

for i in numbers:
    if i%2 == 0:
        even_count += 1
    else:
        odd_count += 1
print(even_count, odd_count)   



#Values above average
#Calculate the average, then count how many values are greater than it. 
numbers = [4, -2, 0, 7, -5, 0, 8]
average = sum(numbers)/len(numbers)   
print("Average is: ", average)
count = 0
for i in numbers:
    if i > average:
        count += 1
print(count)