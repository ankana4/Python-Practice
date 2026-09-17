#Find the Majority Element that occurs more than N/2 times

arr = [7, 0, 0, 1, 7, 7, 2, 7, 7] 
n = len(arr)

#Brute-force approach
key = -1
for i in range(0, n):
    cnt = 0
    for j in range(0, n):
        if arr[j] == arr[i]:
            cnt+=1
    if cnt > n//2:
        key = arr[i]
print(key)        