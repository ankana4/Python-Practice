#189. Rotate Array

#Brute-force approach
def rotateArr(arr, k):
    n=len(arr)
    temp=[]
    if n==0:
        return
    k=n-(k%n)
    for i in range(0, k):
        temp.append(arr[i])
    for i in range(k, n):
        arr[i-k]=arr[i]
    for i in range(n-k, n):
        arr[i]=temp[i-(n-k)]
    return arr

arr=[1, 2, 3, 4, 5, 6, 7]
k=3
print(rotateArr(arr, k))            
    