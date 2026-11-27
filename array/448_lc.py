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