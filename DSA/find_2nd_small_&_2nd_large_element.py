#Find Second Smallest and Second Largest Element in an array
#Brute-force approach

arr = [1, 2, 4, 6, 7, 5]  
n = len(arr)
if n == 0 or n == 1:
    print(-1, -1)
arr.sort()
smallest = arr[1]
largest = arr[n-2]
print("Sorted array is: ", arr)
print("Smallest and largest is: ", smallest, largest)    
