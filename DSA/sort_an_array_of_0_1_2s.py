#Sort an array of 0s, 1s and 2s

#Better approach
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0]
n = len(arr)
c0,c1,c2=0,0,0
for i in arr:
    if i == 0:
        c0 += 1
    elif i == 1:
        c1 += 1
    else:
        c2 += 2
for i in range(0, c0):
    arr[i] = 0
for i in range(c0, c0+c1):
    arr[i] = 1
for i in range(c0+c1, n):
    arr[i] = 2
print(arr)                            

#Optimal approach - Dutch National Flag Algorithm
low = 0
mid = 0
high = n-1

while mid<=high:
    if arr[mid] == 0:
        arr[mid], arr[low] = arr[low], arr[mid]
        low+=1
        mid+=1
    elif arr[mid] == 1:
        mid+=1
    else:
        arr[mid], arr[high] = arr[high], arr[mid]
        high -=1
print(arr)    