#Count of digits in a number

numbers = 32145
c=0
while numbers>0:
    c+=1
    numbers=numbers//10
print(c)