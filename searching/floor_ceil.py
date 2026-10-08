'''
Given a sorted array nums and an integer x. Find the floor and ceil of x in nums. 
The floor of x is the largest element in the array which is smaller than or equal to x. 
The ceiling of x is the smallest element in the array greater than or equal to x. If no floor or ceil exists, 
output -1.
'''

def FloorCeil(arr, x):
    low=0
    floor=-1
    ceil=-1
    high=len(arr)-1
    
    while(low<= high):
        mid=(low+high)//2
        if arr[mid] == x:
            return arr[mid]
        
        elif arr[mid] < x:
            floor=arr[mid]
            low=mid+1
        else:
            ceil=arr[mid]  
            high=mid-1
    return [floor, ceil]

fc=print(FloorCeil([10, 20, 30, 40, 50], 25))          
