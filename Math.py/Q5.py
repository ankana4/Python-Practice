'''
Given a non-negative integer s represented as a string, count the number of digits in s that divide the number represented by s.

A digit is considered valid only if it is non-zero and the number represented by s is divisible by that digit.

If a digit appears multiple times in s, each occurrence should be counted separately.

'''
s = '1122324'
data=int(s)
c=0

for i in s:
    d=int(i)
    if d!=0:
        if data%d==0:
            c+=1
print(c)            