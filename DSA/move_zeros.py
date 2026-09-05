#Move all Zeros to the end of the array

#Brute-force approach

arr = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
temp = []
for i in arr:
    if i != 0:
        temp.append(i)
add_digit = len(arr) - len(temp)
for j in range(0, add_digit):
    temp.append(0)
arr = temp
print(arr)            


#Optimal approach -> two-pointer approach
j = -1
n = len(arr)
for i in range(0, n):
    if arr[i] == 0:
        j = i
        break
for i in range(j+1, n):
    if arr[i]!=0:
        arr[i], arr[j] = arr[j], arr[i]
        j += 1
print(arr)            