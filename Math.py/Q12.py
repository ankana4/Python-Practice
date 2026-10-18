'''
Given two positive integers a and b, return the number of common factors of a and b.

An integer x is a common factor of a and b if x divides both a and b.
'''
c=0
a=6
b=12
for i in range(1, min(a, b)+1):
    if a%i==0 and b%i==0:
        c+=1
print(c)        