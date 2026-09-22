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