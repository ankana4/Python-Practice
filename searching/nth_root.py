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
# print(root)

#Using binary search algo
def mulNum(mid, n, m):
    ans=1
    for i in range(1, n+1):
        ans=ans*mid
        if ans>m: return 2
    if ans==m: return 1
    return 0    
def NthRoot(n, m):
    low=1
    high=m
    while(low<=high):
        mid=(low+high)//2
        func=mulNum(mid, n, m)
        if func==1: return mid
        elif func==0: low=mid+1
        else:
            high=mid-1
    return -1

nRoot=NthRoot(4, 16)    
print(nRoot)    