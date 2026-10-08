'''
Given a sorted array of nums and an integer x, write a program to find the lower bound of x.

The lower bound algorithm finds the first and smallest index in a sorted array 
where the value at that index is greater than or equal to a given key i.e. x.

If no such index is found, return the size of the array.
'''
def lowerBound(arr, x):
    n = len(arr)
    low=0
    high=n-1
    ans=n
    while(low<=high):
        mid=(low+high)//2
        if arr[mid] >= x:
            ans=mid
            high = mid-1
        else:
            low=mid+1
    return ans 
lb = lowerBound([3, 5, 8, 15, 19], 5)
print(lb)
 
          
        