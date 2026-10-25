#Given a sorted array of integers arr and a target value target, 
# count the total number of times target appears in the array. If the target is not present, return 0.

def countOccurance(arr, x):
    count=0
    for value in arr:
        if value==x:
            count+=1
    return count
coo=countOccurance([1, 1, 2, 2 ,2 ,2, 3], 2)     
print(coo)   

