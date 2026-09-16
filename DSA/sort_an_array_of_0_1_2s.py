#Sort an array of 0s, 1s and 2s

#Better approach
arr = [1, 0, 2, 1, 0]
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