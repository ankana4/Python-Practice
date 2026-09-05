#Problem Statement: Given an array, and an element num the task is to find if num is present in the given array or not. If present print the index of the element or print -1.
arr = [5, 4, 3, 2, 1]
num = 5

n = len(arr)
index=-1
for i in range(0, n):
    if arr[i] == num:
        index=i
        break
print(index)    