'''
Given a positive integer n. Find and return its square root. 
If n is not a perfect square, then return the floor value of sqrt(n).

'''
#Brute-force approach
def floorSqrt(n):
    ans=1
    for i in range(1, n):
        if i*i<=n:
            ans=i
        else:
            break
    return ans
fs=floorSqrt(38)
print(fs)
          
#Using binary search algorithm
def mySqrt(n):
    ans=1
    low=1
    high=n
    if n==0:
        return 0
    while low<=high:
        mid=(low+high)//2
        if mid*mid<=n:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans                   
ms=mySqrt(35)
print(ms) 
