#287. Find the Duplicate Number

#Better approach
def findDuplicates(nums):
    temp_dict={}
    for i in nums:
        if i not in temp_dict:
            temp_dict[i]=1
        else:
            temp_dict[i]+=1
            
    for k, v in temp_dict.items():
        if v>1:
            return k

nums=[3,3,3,3,3]
print(findDuplicates(nums))            