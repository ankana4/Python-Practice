#Check if a number is Palindrome or Not
n = 4554
rev = 0
compare = n
while n>0:
    last_digit = n%10
    rev = rev*10+last_digit
    n = n//10
if rev == compare:
    print("Palindrome")
else:
    print("Not Palindrome")        
  