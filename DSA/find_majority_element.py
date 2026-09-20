#Find the Majority Element that occurs more than N/2 times

arr = [7, 0, 0, 1, 7, 7, 2, 7, 7] 
n = len(arr)

#Brute-force approach
key = -1
for i in range(0, n):
    cnt = 0
    for j in range(i, n):
        if arr[j] == arr[i]:
            cnt+=1
    if cnt > n//2:
        key = arr[i]
print(key)       

#Better Approach
temp_dict={}

for i in arr:
    if i in temp_dict:
        temp_dict[i]+=1
    else:
        temp_dict[i] =1
max_key = -1
for k, v in temp_dict.items():
    if v > n//2:
        max_key = k
print(max_key)                    
 

#Optimal aaproach -> Moore's voting algorithm 
c=0
el=0
for i in range(0, n):
    if c == 0:
        c = 1
        el=arr[i]
    elif el == arr[i]:
        c == 1
    else:
        c -=1  
c1 = arr.count(el)
key = -1       
if c1 > n//2:
    key = el
print(key)        