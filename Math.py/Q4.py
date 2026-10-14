'''
Given a positive integer n, find the number of perfect squares that are less than n in the sample space of perfect squares. 
The sample space consists of all perfect squares starting from 1 (i.e., 1, 4, 9, 16, 25, …)
'''
n = int(input("Enter a number: "))
c=0
for i in range(1, n+1):
    if i*i<n:
        c+=1
print(c)        
        