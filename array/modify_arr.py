#Modify an array such that if 'arr[i]' is 'j' then arr[j] becomes i
#Brute-force approach
def reArrange(arr):
    n=len(arr)
    newArr=[0]*n
    
    for i in range(n):
        newArr[arr[i]]=i
    for i in range(n):
        arr[i]=newArr[i]
    return arr

arr=[2, 0, 1, 4, 5, 3]
print(reArrange(arr))           