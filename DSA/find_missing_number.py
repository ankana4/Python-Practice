#Find the Missing Number

#Linear search for missing number

arr= [8, 2, 4, 5, 3, 7, 1]
n = len(arr)
data = -1
for i in range(1, n):
    found = False
    for j in range(0, n):
        if arr[j] == i:
            found = True
            break
    if not found:
        data=i
print(data)            


#Using set
seen = set(arr)
for i in range(1, n):
    if i not in seen:
        print(i)
        break
    
#Using Sum of n terms Formula    
n = len(arr)+1
totalSum = sum(arr)
expectedSum = n * (n+1) //2

missingNum = expectedSum - totalSum
print(missingNum)

#Brute-force approach
arr.sort()
num = 0
for i in range(0, len(arr)):
    if arr[i]+1 != arr[i+1]:
        num = arr[i]+1
        break
print(num)    