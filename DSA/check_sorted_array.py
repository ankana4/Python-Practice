#Check if an Array is Sorted
arr = [1,2,3,4,5]
n = len(arr)
isSorted = True

for i in range(0, n-1):
    if arr[i] > arr[i+1]:
        isSorted = False
        break
    
if isSorted:
    print("True")
else:
    print("False")             