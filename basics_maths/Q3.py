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
  
  #Another approach
  
def is_palindrome(n):
    rev = 0
    dup = n
    while n>0:
        last_digit = n%10
        rev = rev*10+last_digit
        n = n//10  
    return rev == dup

n = 455
if is_palindrome(n):
    print("Palindrome")
else:
    print("Not Palindrome")    