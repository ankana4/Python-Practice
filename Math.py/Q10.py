'''
Given a number n. Return true if the digit sum(or sum of digits) of n is a Palindrome number otherwise false.
A Palindrome number is a number that stays the same when reversed.
'''
n = 98
digit_sum=0
while n>0:
    digit_sum+=n%10
    n=n//10
original=digit_sum
rev=0
while digit_sum>0:
    ld=digit_sum%10
    rev=rev*10+ld
    digit_sum=digit_sum//10
print(original==rev)        
           
    