#Count Maximum Consecutive One's in the array

arr = [1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1]
c = 0
maxC=0
n = len(arr)

for i in range(0, n):
    if arr[i] == 1:
        c += 1
        maxC = max(maxC, c)
    else:
        c = 0
print(maxC)            
    