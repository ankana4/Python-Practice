arr = [1,0,2,3,0,4,5,0]

i=0
while(i<len(arr)):
    if arr[i] == 0:
        for j in range(len(arr)-1, i, -1): #[1,0,0,2,3,0,4,5]
            arr[j] = arr[j-1]
        i += 1
    i+=1
print(arr)          
            
