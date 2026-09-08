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

#Two-pointer approach
m = len(arr1)
n = len(arr2)
i,j=0,0

union_list=[]
while i<m and j<n:
    if arr1[i]<arr2[j]:
        if not union_list or union_list[-1] != arr1[i]:
            union_list.append(arr1[i])
        i+=1
        
    elif arr2[j]<arr1[i]:
        if not union_list or union_list[-1] != arr2[j]:
            union_list.append(arr2[j])
        j+=1    
    
    else:
        if not union_list or union_list[-1] != arr1[i]:
            union_list.append(arr1[i])
        i+=1
        j+=1    
while i<n:
    if not union_list or union_list[-1] != arr1[i]:
            union_list.append(arr1[i])
    i+=1
while j<m:
    if not union_list or union_list[-1] != arr2[j]:
                union_list.append(arr2[j])
    j+=1

print(union_list)    
                            