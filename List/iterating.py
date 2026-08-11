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
    
    
#Conditional printing
#Print only values greater than 20.   
numbers = [10, 20, 30, 40]
for i in range(len(numbers)):
    if numbers[i] > 20:
        print(numbers[i]) 
    
    
#Even indexes
#Print values at even indexes. Do not confuse even indexes with even values.  
for i in range(0, len(numbers), 2):
    print(f"Numver at index {i} is {numbers[i]}")  
    


#Stop at first negative
#Use break to stop before printing the negative number.
numbers = [10, 20, 30, -5, 40, 50]    

for i in range(len(numbers)):
    if numbers[i] < 0:
        break
    print(numbers[i])