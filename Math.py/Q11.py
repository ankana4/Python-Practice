#Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
n=0
while(n>=10):
    digit_sum=0
    while n>0:
        digit_sum+=n%10
        n=n//10
    n=digit_sum
print(n)        