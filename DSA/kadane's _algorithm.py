arr = [-2, -3, 4, -1, -2, 1, 5, -3]

#Brute-force approach
n = len(arr)
ml = 0

for i in range(0, n):
    s=0
    for j in range(i, n):
        s += arr[j]
        ml = max(ml, s)
print(ml)        

#Optimal approach - Kadane's algorithm
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
n = len(arr)
maxi = float('-inf')
summ = 0

start = 0
ansStart = -1
ansEnd = -1

for i in range(0, n):
    if summ == 0:
        start = i
    summ += arr[i]
    if summ > maxi:
        maxi=summ
        ansStart = start
        ansEnd = i
    if summ < 0:
        summ = 0
print(maxi)
print("Subarray: ", arr[ansStart:ansEnd + 1])               
