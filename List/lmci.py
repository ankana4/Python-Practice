'''
Length, Membership, Count, and Index
'''
#List length
#Find the number of elements using len().

numbers = [10, 20, 30, 40]
print(len(numbers))


#Length without len()
#Count elements manually using a loop.
numbers = [10, 20, 30, 40, 50]
c = 0
for i in numbers:
    c+=1
print(c)

#Membership
#Check whether 30 exists using in.
numbers = [10, 20, 30, 40]
if 30 in numbers:
    print("Yes")
    
#Non-membership
#Check whether 100 is absent using not in.
numbers = [10, 20, 30, 40]
if 100 not in numbers:
    print("No")
    
    
#Count without count()
#Count how many times 5 occurs.
numbers = [5, 2, 5, 8, 5, 9]    
c = 0
for i in numbers:
    if i ==5:
        c+=1
print(c)        

#Index without index()
#Find the first index of 30.
numbers = [10, 20, 30, 40]
for i in range(len(numbers)):
    if numbers[i] == 30:
        print(i)
        break

#Missing element handling
#Print "Element not found" instead of raising an error.
numbers = [10, 20, 30, 40]
try:
    print(numbers[10])
except IndexError:
    print("Element not found")