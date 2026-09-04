#Rotate array by K elements
#brute-force approach
arr = [1, 2, 3, 4, 5, 6, 7]
n = len(arr)
d=3
temp = []
d = d%n

#stored first d elements
for i in range(0, d):
    temp.append(arr[i])
print(temp)    

#shift remaining elements to the left
for i in range(d, n):
    arr[i-d] = arr[i]
print(temp)    

#put temp variables at the end
for i in range(n-d, n):
    arr[i] = temp[i-(n-d)]
print(arr)    


#Optimal approach
d=d%n

#reverse whole array
arr.reverse()

#first reverse first 3 elements
arr[:d] = reversed(arr[:d])

#second reverse remaining element
arr[d:] = reversed(arr[d:])

print(arr)