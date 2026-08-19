#Reverse a number
n = 12345
rev = 0
while n>0:
    last_digit = n%10
    rev = rev*10+last_digit
    n = n//10
print(rev)    