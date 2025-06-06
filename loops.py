'''
Loops are usedto repeat a block of code
There are two types of loops in python ->
for loop, while loop
'''

#Example 1:

for i in range(1, 6):
    print(i)
print("task complete ", i)    

#Loop through a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
print(f"I like {fruits[0]}")    

#Loop through a string
word = "Python"
for char in word:
    print(char)

#Using range to loop over numbers
for i in range(5):
    print(i)

for i in range(2, 11, 2):  #2,3,4,5,6,7,8,9,10
    print(i) #2, 4, 6, 8, 10 even number
    
#Odd number
for i in range(1, 11, 2):  #1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    print(i) # 1, 3, 5, 6, 9   

#Loop with index using enumerate()

colors = ["red", "green", "yellow"]

for index, color in enumerate(colors):
    print(f"{index} : {color}")

#Enumerate example :
'''
In python enumerate() is a build-in function used with iterables(lists, tuple, string, dic etc)
syntax : enumerate(iterable, start=0)
'''

#Example 1:
fruits = ("apple", "mango")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index} : {fruit}")

#Example 2:
with open("data.txt") as file:
    for line, i in enumerate(file, start=1):
        print(f"{line} : {i}")
        

#Nested for loops
for i in range(1, 4):  #1, 2, 3
    for j in range(1, 4):  #1, 2, 3, 1, 2, 3, 1, 2, 3
        print(f"{i} * {j} = {i * j}")

#Parsing json-like data
data = [
    {"user": "Alice", "active": True},
    {"user" : "Bob", "active": False},
    {"user": "Charlie", "active": True}
]                

for record in data:
    if record['active']:
        print(f"Active : {record["user"]}")

#Generating reports from logs
logs = [
    "INFO: Server started",
    "ERROR: Failed to connect to DB",
    "INFO: Request received",
    "ERROR: Timeout"
]

error_count = 0

for log in logs:
    if log.startswith("ERROR"):
        print(log)
        error_count += 1
print(f"Total errors are {error_count}")        

#Working with zip()

names = ["Alice", "Bob", "John"]
scores = [90, 95, 88]
groups = (1,2), (1,2,3)

for name, score, group in zip(names, scores, groups):
    print(f"{name} : {score} : {group}")


#Patterns

'''
*
**
***
****
*****
'''

for i in range(1, 6):
    print("*" * i)
    

'''
1
12
123
1234
''' 

for i in range(2, 6):    #i=2
    for j in range(1, i):      #j=1, 3
        print(j, end='') # 1 1 2 
    print()        

'''
4321      #4, 0
432       #4, 1
43        #4, 2
4         #4, 3
'''

for i in range(0, 4):  #i=0
    for j in range(4, i, -1):  #j=4,0->4
        print(j, end="")
    print()    


'''
1234   1, 5
123    1, 4
12     1, 3
1      1, 2
'''  

for i in range(5, 1, -1):  # i = 5, 4
    for j in range(1, i):  #j=1, 5
        print(j, end="")
    print()    

'''
4321    4, 0
321     3, 0
21      2, 0
1       1, 0
'''

for i in range(4, 0, -1):  #i=5, 4, 3, 2
    for j in range(i, 0, -1):  #j=(4,0,-1)->4321, (3,0,-1)->3,2,1, (2,0,-1)->2,1, (1, 0, -1)->1
        print(j, end="")
    print()    


'''
1        
22       
333      
4444     
'''

for i in range(1, 5):     #i=1, 2
    for j in range(1, i+1):  #(3, 4)
        print(i, end="")
    print()    

'''    
4444
333
22
1
1        
22       
333      
4444      
'''

for i in range(4, 0, -1):  
    for j in range(0, i):
        print(i, end="")
    print()        

for i in range(1, 5):
    for j in range(1, i+1):
        print(i, end="")    
    print()    
    
    