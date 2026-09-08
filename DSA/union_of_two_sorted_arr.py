#Union of Two Sorted Arrays

arr1 = [1,2,3,4,5]
arr2 = [2,3,4,4,5]
seen = set()
for i in arr1:
    seen.add(i)
for i in arr2:
    seen.add(i)
print(seen)        

#Another approach using set()
st = set(arr1) | set(arr2)
print(sorted(st))