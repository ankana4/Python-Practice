#Max Circular Subarray Sum

#Brute-force approach
def maxCircularArray(arr):
    n=len(arr)
    largest=arr[0]
    for i in range(n):
        total=0
        for j in range(n):
            index=(i+j)%n
            total+=arr[index]
            
            if total>largest:
                largest=total
    return largest

arr=[8, -8, 9, -9, 10, -11, 12]
print(maxCircularArray(arr))           