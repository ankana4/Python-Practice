from typing import List
from collections import defaultdict

def longest_arith_seq_length(nums: List[int]) -> int:
    n = len(nums)
    if n <= 2:
        return n
    
    dp = [defaultdict(int) for _ in range(n)]
    max_len = 0

    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]
            # Either extend the sequence or start new with length 2
            dp[i][diff] = dp[j][diff] + 1 if diff in dp[j] else 2
            max_len = max(max_len, dp[i][diff])

    return max_len
print(longest_arith_seq_length([3, 6, 9, 12]))      
print(longest_arith_seq_length([9, 4, 7, 2, 10]))    
print(longest_arith_seq_length([20, 1, 15, 3, 10, 5, 8]))


fruit = ["apple", "banana", "guava"]
print(fruit)

access_fruit = fruit[1]
print(access_fruit)

update_item = fruit[2]
print(update_item)

fruit[2] = "cherry"
print(fruit)

a = fruit.append("kiwi")  #list.append() does not return the updated list
print(a)

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

result.remove(result[1])
print(result)
result[0].remove('pie')
print(result)


list = [0,2,3,4,5,6,7]
for i in list:
    list.remove(i)
print(list)    

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
    

a = [1, 2, 3, 4]
l = [c ** 2 for c in a] 
print(l)       

def even(a):
    return a%2==0

f = [1, 2, 3, 4, 5, 6]
d = filter(even, f)
print(list(d))


s = ['1', '2', '3', '4', '5']
res = map(int, s)
print(list(res))


class Dog:
    species = 'lab'
    
    def __init__(self, name):
        self.name = name
dog = Dog('lll')
print(dog.name)    
dog.species = 'kiwi'    
print(dog.species)


class Dog:
    def __init__(self, name, age):
        self.name=name
        self.age = age
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        
d = Dog('OOOO', 23)
print(d.name, d.age)            


class Animal:
    def sound(self):
        print("Bark")
        
class Dog(Animal):
    def sound(self):
        print("Woof")
        return "hii"

a = Animal()        
d = Dog()
print(d.sound())
# print(a.sound())
                
from abc import ABC, abstractmethod                
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass  
    
class Dog(Animal):
    def sound(self):
        print("Woop") 
        return "Woof"
        
d1 = Dog()
print(d1.sound())                     

class Parent():
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print(self.name)
        
    
    def display(self, post):
        self.post = 'SDE'
        return post 
    
class Child(Parent):
    def display(self,name,age):
        print(self.name)
        

s1 = Child("Ankana", 27)
print(s1.age)       
num=321
def reverse_number(num):
    rev_data = 0
    if num<0:
        num = num * -1  #321
        while(num>0):
            lastDigit = num % 10  #3
            rev_data = rev_data*10 + lastDigit #12
            rev = rev_data * -1  #-12
            num=num // 10 
            
    else:
        while(num > 0):
            lastDigit = num % 10
            rev_data = rev_data*10 + lastDigit
            rev = rev_data
            num=num // 10 
                
    return rev   
number = reverse_number(321)
print(number)