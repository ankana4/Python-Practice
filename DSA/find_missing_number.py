#Find the Missing Number

#Linear search for missing number

arr= [8, 2, 4, 5, 3, 7, 1]
n = len(arr)+1

for i in range(1, n):
    found = False
    for j in range(0, n-1):
        if arr[j] == i:
            found = True
            break
    if not found:
        print(i)
print(-1)            