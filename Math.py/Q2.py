'''
Given a number n, determine whether it is a prime number or not.
Note: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
'''
n=8
if n<=1:
    print("False")
if n==2:
    print("True")
if n%2==0:
    print("False")
i=3
while i*i<=n:
    if n%i==0:
        print("False")
    i+=2
print("True")     