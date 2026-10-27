'''
Given two numbers N and M, find the Nth root of M. 
The Nth root of a number M is defined as a number X such that when X is raised to the power of N, it equals M. 
If the Nth root is not an integer, return -1.

'''
#Brute-force approach
def NthRoot(n, m):
    ans=1
    i=1
    while i<=m:
        ans=i**n
        if ans==m:
            return i
        elif ans>m:
            break
        i+=1
    return -1  
root=NthRoot(5, 32)      
print(root)