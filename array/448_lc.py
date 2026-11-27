#448. Find All Numbers Disappeared in an Array

#Brute-force approach
def findDisappeardNumbers(nums):
    n=len(nums)
    result=[]
    for i in range(1, n+1):
        if i not in result:
            result.append(i)
    return result
nums=[1,1]
print(findDisappeardNumbers(nums))        


#Better approach
def findDisappeardNumbers(nums):
    n=len(nums)
    result=[]
    seen=set(nums)
    
    for i in range(1, n+1):
        if i not in seen:
            result.append(i)
    return result

nums=[4,3,2,7,8,2,3,1]
print(findDisappeardNumbers(nums))         