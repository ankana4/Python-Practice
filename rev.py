# from typing import List
# from collections import defaultdict

# def longest_arith_seq_length(nums: List[int]) -> int:
#     n = len(nums)
#     if n <= 2:
#         return n
    
#     dp = [defaultdict(int) for _ in range(n)]
#     max_len = 0

#     for i in range(n):
#         for j in range(i):
#             diff = nums[i] - nums[j]
#             # Either extend the sequence or start new with length 2
#             dp[i][diff] = dp[j][diff] + 1 if diff in dp[j] else 2
#             max_len = max(max_len, dp[i][diff])

#     return max_len
# print(longest_arith_seq_length([3, 6, 9, 12]))      
# print(longest_arith_seq_length([9, 4, 7, 2, 10]))    
# print(longest_arith_seq_length([20, 1, 15, 3, 10, 5, 8]))


fruit = ["apple", "banana", "guava"]
print(fruit)

access_fruit = fruit[1]
print(access_fruit)

update_item = fruit[2]
print(update_item)

fruit[2] = "cherry"
print(fruit)

# a = fruit.append("kiwi")  #list.append() does not return the updated list
# print(a)

new_list = ["mango", "pie"]
fruit.extend(new_list)
new_item = ("chilli","ppp")
fruit.extend(new_item)
print(fruit)


list1 = ['a', 'b', 'c']
new_data = fruit + list1
result= list((list1, fruit, new_item, []))
result = []
result.append(fruit)
result.extend(['apple'])
print(result)

# result.remove(result[1])
# print(result)
# result[0].remove('pie')
# print(result)


# list = [0,2,3,4,5,6,7]
# for i in list:
#     list.remove(i)
# print(list)    

list1 = ['a']
list2 = ['b', 'c']
list3 = ['d', 'e']

new_list1 = [*list1, '1','2', *list2, *list3]
print(new_list1)

import copy
original = [['apple', 'banana', 'cherry', 'mango', 'pie', 'chilli', 'ppp']]
copyyy = copy.deepcopy(original) 
copyyy[0][0] = 'oooo'
print("Original ", original)
print(copyyy)

def unpack_data(a, b, c):
    print(a, b, c)

data = (1, 2, 3)
unpack_data(*data)
    
