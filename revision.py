n = 100
for i in range(1, n+1):
    if i % 2 == 0:
        print("Even", i)
    else:
        print("Odd")
            
n = 1156
total_sum = 0
while(n>0):
    last_digit = n%10
    total_sum = total_sum + last_digit
    n = n // 10
print(total_sum)                

n = 3
for i in range(1, 11):
    mul = n * i
    print(mul)    

s = 'aabbeio'
c = 0
for i in s:
    if i in ['a', 'e', 'i', 'o', 'u']:
        c = c+1
print(c)        

for i in range(1, 51):
    if i%3==0 and i%5==0:
        print("FizzBuzz", i)       
    if i%3 == 0:
        print("Fizz", i)
    elif i%5 == 0:
        print("Buzz", i) 

s = [11, 12, 44, 55]
new_list = []
for i in range(len(s), 0, -1):
    new_list.append(s[i-1])
print(new_list)    

s = [44, 101, 11, 98]
result = s[0]
for i in range(1, len(s)):
    if s[i] > result:
        result = s[i]
print(result)            

s = [1, 2, 1, 5, 6, 2]
new_list = []
for i in s:
    if i not in new_list:
        new_list.append(i)
print(new_list)        

t = (2, 4, 6, 7)
sum1 = 0
for i in t:
    sum1 = sum1+i
print(sum1)    

s = [9, 4, 6, 8]
f=0
t=0
l = len(s)-1
for i in range(0, len(s)):
    if f < l:
        t = s[f]
        s[f] = s[l]
        s[l] = t
        f += 1
        l -= 1
print(s)        
        
        
s1 = [4, 7, 8, 9]
s2 = [2, 5, 6, 7]        
new_list = []
for i in s1:
    new_list.append(i)
for i in s2:
    new_list.append(i)
print(new_list)        
    
    
s = 'i am a girl'
dict1 = {}
for i in s:
    if i == " ":
        continue
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] += 1
print(dict1)            
        
        
students = {}
for i in range(2):
    name = input("Enter a name: ")
    marks = input("Enter marks: ")
    students[name] = marks 
print(students)    

students = {'john': 92, 'putu': 87, 'tanu': 77, 'gitu': 43}
no_of_students = len(students)
print(no_of_students)
marks = 0
for key, val in students.items():
    marks = marks+val
    total_sum = marks
average_marks = total_sum/no_of_students
print(average_marks)    


item = {'a':45, 'b': 30, 'c': 55}
result = item['a']
for key, val in item.items():
    if item[key] > result:
        result = item[key]
print(result)                   

s = 'momi'
data = ''
for i in s[::-1]:
    data = data+i
if data == s:
    print("Palidrome")
else:
    print("Not")        


a = 'aabb'
b = 'abab'

if len(a) != len(b):
    print("Not anagram")
else:
    for ch in a:
        if a.count(ch) != b.count(ch):
            print("Not anagram")
    print("Anagram")        

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

list1 = []
for i in range(1, 6):
    list1.append(i)
print("list",list1)    

a = 0
b = 6
op = '_'

if op == '+':
    result = a+b
elif op == '-':
    result = a-b
elif op == '*':
    result = a*b
elif op == '-':
    result = a/b
else:
    result = "Wrong operand is used"       
print(result)          

list1 = [1, 2, 3, 6]
list2 = [1, 3, 4, 6]
new_list = []
for i in list1:
    if i in list2:
        new_list.append(i)
print(new_list)        


student = {
"name": "Alice",
"grades": {"math": 90, "science": 80}
}

student['name'] = 'Alice'
student['grades'] = {"math": 90, "science": 80}
print(student['grades']['math'])
