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
    
    
#Better approach

def reverse(nums, start, end):
    n=len(nums)
    while start<end:
        nums[start], nums[end] = nums[end], nums[start]
        start+=1
        end-=1
        
def rotateArr(arr, k):
    n=len(arr)
    k=k%n
    if n==0 or k==0:
        return arr
    reverse(arr, 0, n-1)
    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)
    return arr

arr=[1, 2, 3, 4, 5, 6, 7, 8]
d=3
print(rotateArr(arr, d))
        