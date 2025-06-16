#Write a program that prints all even numbers from 1 to 100.
n = 100
for i in range(1, n+1):
    if i % 2 == 0:
        print(f"Even number {i}")
   
#Take an integer input and print the sum of its digits.
n = int(input("Enter a number : ")) 
sum = 0

while n>0:          
    num = n % 10    
    sum = sum + num   
    n = n // 10  
        
print(f"Sum of digit is : {sum}")     

#Ask the user for a number and print its multiplication table up to 10.
n = int(input("Enter a number "))
for i in range(1, 11):
    print(f"Multiplication of {i} is : {n * i}")

#Take a string input and count how many vowels are in it.
data = str(input("Enter a word : "))
count = 0
for ch in data:
    if ch == 'A' or ch == 'a':
        print(ch)
        count += 1
    elif ch == 'E' or ch == 'e':
        print(ch)
        count += 1
    elif ch == 'I' or ch == 'i':
        print(ch)
        count += 1
    elif ch == 'U' or ch == 'u':
        print(ch)
        count += 1
    elif ch == 'O' or ch == 'o':
        print(ch)  
        count += 1    
print(f"Count of vowel is {count}") 

#Optimize approach
data = input("Enter a string : ")
count = 0

for ch in data:
    if ch  in ['A', 'E', 'I', 'O', 'U'] or ch in ['a', 'e', 'i', 'o', 'u']:
        count += 1
print(f"No of vowels {count}")       

                        
#Print numbers from 1 to 50. For multiples of 3, print "Fizz", for multiples of 5, print "Buzz", and for both, print "FizzBuzz".  
n = 50
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")                              


#Write a function that takes a list and returns a new list with elements reversed.
#Without using [::-1] or .reverse().

list = [10, 20, 30, 40, 50]
new_list = []
for i in range(len(list), 0, -1):
    new_list.append(list[i-1])
print(f"new list {new_list}")
    
# Without using new list(In Place)
list = [10, 20, 30, 40, 50]
first_idx = 0
last_idx = len(list)-1
for i in list:
    if first_idx < last_idx:
        temp = list[first_idx]
        list[first_idx] = list[last_idx]
        list[last_idx] = temp
        first_idx += 1
        last_idx -= 1
print(list)

#Given a list of numbers, find and print the maximum number (without using max()).
list = [10, 20, 30, 51, 50]
result = list[0]
for i in range(1, len(list)): 
    if list[i] > result:
        result = list[i]
print(f"Maximum number is {result}")        
    

#Write a program that removes duplicates from a list and keeps only the first occurrence.    
list = ['apple', 'kiwi', 'apple', 'mango', 'banana']   
new_list = []
for ch in list:
    if ch not in new_list:
        new_list.append(ch)
print(new_list)    


#Take a tuple of numbers and return the sum of all elements.
num = (1, 2, 3, 4, 5)
sum = 0
for i in num:
    sum = sum + i
print(f"Sum of all elements {sum}")    


#Write a function that merges two lists into one without using + or extend().
list1 = ['Navin', 'Tarun']
list2 = ['Barun', 'Rabi', 'Sita']
updated_list = []
for name in list1:
    updated_list.append(name)
for name in list2:
    updated_list.append(name)    
print(updated_list)    


#optimize approach, unpack values
list1 = ['Navin', 'Tarun']
list2 = ['Barun', 'Rabi', 'Sita']
updated_list = [*list1, *list2]
print(updated_list)
    
#Ask the user to input a sentence. Count the frequency of each word and print it as a dictionary.
dict = {}
# word = input("Enter a sentence : ")
word = 'I have a word with you'
for i in range(len(word)):
    c = word.count(word[i])
    print(c)
    dict[i] = word[i]
print(dict)        
    
#Create a dictionary where keys are student names and values are their marks. Then calculate the average mark.
data = {'Amrit': 30, 'Sruti': 55, 'Sristi': 87, 'Paran': 76}
no_of_students = len(data)
sum = 0
for key, value in data.items():
    marks = value
    sum = sum + value
    total_marks = sum / no_of_students
print(total_marks)      


#Given a dictionary of item: price, find the item with the highest price.
item_prices = {
    "apple": 30,
    "banana": 10,
    "milk": 45,
    "bread": 40,
    "eggs": 60
}

result = item_prices['apple']
for key, val in item_prices.items():
    if item_prices[key] > result:
        result = item_prices[key]
print(result)        


# 4. Write a function that checks if a given string is a palindrome (same forwards and backwards).
str_data = 'mom'
temp = ''
for ch in str_data[::-1]:
    print(ch)
    temp = temp + ch
if str_data == temp:
    print('Palindrome')
else:
    print('Not palindrome')  


#Write a function that checks if two words are anagrams (contain the same letters in different order)
str_data1 = 'aabb'
str_data2 = 'bbaa'
temp = ''
if len(str_data1) != len(str_data2):
    print("Not anagram")
else:
    for ch in str_data1:
        if str_data1.count(ch) != str_data2.count(ch):
            print('Not anagram')
    print('Anagram')         


#Write your own version of the range() function that returns a list of numbers between two values.
def get_list(a, b):
    data = []
    a += 1
    while a < b:
        data.append(a)
        a += 1
    return data

a = 0
b = 6

list_data = get_list(a, b)
print(list_data)


#Create a calculator that takes two numbers and an operator (+, -, *, /) and returns the result.
def calculator(a, b, op):
    data = None
    if op == '+':
        data = a + b
    elif op == '-':
        data = a - b
    elif op == '*':
        data = a * b
    elif op == '/':
        try:
            data = a / b  
        except ZeroDivisionError as e:
            print(str(e))   
    else:
        print(f'You take wrong operator, Please select correct one{'+', '_', '*', '/'}')                   
    return data

try:
    a = int(input("Enter a : "))
    b = int(input("Enter b : "))
    op = input("Enter operator : ")
    result = calculator(a, b, op)
    print(result)

except ValueError as e:
    print(f'Incorrect input provided, {str(e)}')    


#Given two lists, print a list of elements common to both.    
a = [1, 2, 3, 4, 5, 2]
b = [2, 4, 6, 7, 8]
list = []
for data in a:
    if data in b and data not in list:
        list.append(data)
print(list)         


#4. Create a dictionary like this:
'''
student = {
"name": "Alice",
"grades": {"math": 90, "science": 80}
}
'''

# Then write code to print only the math grade.

student = {}
student['name'] = 'Alice'
student['grades'] = {"math": 90, "science": 80}
print(student['grades']['math'])
no_of_sub = len(student['grades'])
total_sum = 0
for key, value in student['grades'].items():
    total_sum = total_sum + value #170
total_avg = total_sum/no_of_sub #170/2
print(total_avg)   