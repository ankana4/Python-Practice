#Find the Largest element in an array
#1.Using Bubble sort approach - brute force appraoch

nums = [2, 5, 1, 3, 0]
largest = nums[0]
n = len(nums)
for i in range(0, n):
    didswapped=False
    for j in range(0, n-i-1):
        if nums[j] < nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            didswapped=True
    if not didswapped:
        break
print(nums)
print(nums[0])            
            
#Better appraoch
largest = nums[0]
for i in range(1, n):
    if nums[i] > largest:
        largest = nums[i]
print(largest)                    