#215. Kth Largest Element in an Array
#Brute-force appraoch
nums = [3,2,1,5,6,4]
k = 2
n = len(nums)
for i in range(0, n):
    didswapped=False
    for j in range(0, n-i-1):
        if nums[j] < nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            didswapped=True
    if not didswapped:
        break
print(nums[k-1])            
    
    
#Optimal appraoch using minheap
import heapq
heap=[]
for i in nums:
    heapq.heappush(heap, i)
    if len(heap)>k:
        heapq.heappop(heap)
print(heap[0])            