'''
Kth smallest element in the array using constant space when array can't be modified
'''
#Brute-force approach
def KthSmallestEle(arr, k):
    if k<1 or k>len(arr):
        return -1
    previous=float('-inf')
    for i in range(0, k):
        current=float('inf')
        for j in range(0, len(arr)):
            if previous<arr[j]<current:
                current=arr[j]
        previous=current
    return previous

smallest_ele=KthSmallestEle([7, 10, 4, 3, 20, 15], 3)      
print(smallest_ele)      