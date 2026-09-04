#Find Second Smallest and Second Largest Element in an array
#Brute-force approach

arr = [1, 2, 4, 7, 7, 5]  
n = len(arr)
if n == 0 or n == 1:
    print(-1, -1)
arr.sort()
smallest = arr[1]
largest = arr[n-2]
print("Sorted array is: ", arr)
print("Smallest and largest is: ", smallest, largest)    

#Better approach
#First find largest element
largest = arr[0]
for i in range(1, n):
    if arr[i] > largest:
        largest = arr[i]

#Now find second largest
second_largest = -1
for i in range(0, n):
    if arr[i] > second_largest and arr[i] != largest:
        second_largest = arr[i]
print(second_largest)            

#Find smallest
smallest = arr[0]
for i in range(1, n):
    if arr[i] < smallest:
        smallest = arr[i]

#Second smallest
second_smallest = float('inf')   
for i in range(1, n):
    if arr[i] < second_smallest and arr[i] != smallest:
        second_smallest = arr[i]
print(second_smallest)        


#Optimal approach for second largest
largest = arr[0]
slargest = -1
for i in range(1, n):
    if arr[i] > largest:
        slargest = largest
        largest = arr[i]
    elif arr[i] < largest and arr[i]>slargest:
        slargest = arr[i]
print(second_largest)            
    
#Optimal approach for second smallest
smallest = arr[0]
ssmallest = float('inf')
for i in range(1, n):
    if arr[i]<smallest:
        ssmallest = smallest
        smallest = arr[i]
    elif arr[i] != smallest and arr[i] < ssmallest:
        ssmallest = arr[i]
print(ssmallest)        
    