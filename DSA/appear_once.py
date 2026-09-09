#Find the number that appears once, and the other numbers twice
arr = [4,1,2,1,2]
freq = {}

#Brute-force approach

for num in arr:
    if num in freq:
        freq[num] = freq[num]+1
    else:
        freq[num] = 1
            
for num in freq:
    if freq[num] == 1:
        print(num)            

#Another brute-force approach        
n = len(arr)
for i in range(0, n):
    num = arr[i]
    c = 0
    for j in range(0, n):
        if arr[j] == num:
            c += 1
    if c == 1:
        print(num)                