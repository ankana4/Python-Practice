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
          
        