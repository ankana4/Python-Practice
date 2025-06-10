# '''
# Dictionary - It is a collection of key-value pair
# Each key is unique and it maps to a value
# A dictionary is an associative array(Associative array is a data structure
# that stores data in the form of key-value pairs)
# '''

# #Example 1
# my_dict = {"name": "John", "age": 25, "city": "New York"}
# print(my_dict)

# user_dict ={}
# for i in range(2):
#     key = input("Enter key: ")
#     value = input("Enter value: ")
#     user_dict[key] = value
# print(user_dict)    

# student = {}
# for i in range(2):
#     name = input("Enter the name : ")
#     age = int(input(f"Enter the age {i+1} : "))
#     student[name] = age
# print(student)

# #Accessing Values
# student = {
#     "name1": "John",
#     "age1": 20,
#     "course1": "Computer Science",
#     "name2": "Asus",
#     "age2": 20,
#     "course2": "Computer Science",
#     "name3": "LINUX",
#     "age3": 20,
#     "course3": "Computer Science",
    
# }
# print(student["name1"])  
# print(student.get('name'))
# print(student.get('name', 'Not Found'))  

# #Looping through a dictionary

# for key, values in student.items():
#     print(key, "->", values)

# #Dictionary methods
# print(student.keys())  #Print list of keys 
# print(student.values())  #Print list of values
# print(student.items())   #Return list of tuples contain key and its associated values

# #List of dictionary

# keys = ['Navin', 'Kiran', 'Harsh']
# values = ['Python', 'Java', 'C']
# print(keys)
# print(values)

# data = dict(zip(keys, values))
# print(data)
# print(data['Kiran'])

# #Add data in dictionary
# data['Monica'] = 'Java'
# data['Asus'] = 'C'
# print(data)

# #Delete data from dictionary
# del data['Monica']            # Del does not return anything
# print(data)
# my_values = data.pop('Monica')  # Pop returns the value of removed key
# print(my_values)
# print(data)

# print(data.pop('Suku', 'Not Found'))  #Avoid error by passing default value

# #Create dictionary with dictionary and lists
# prog = {'JS': 'Atom', 'CS': 'VS', 'Python': ['Pycharm', 'Sublime'], 'Java': {'JSE':'NetBeans', 'JEE': 'Eclipse'}, 'Name':{'name1':{'subname1':{'Ankana':[20, 22, 25],'Gaurav': 22}}}}
# print(prog['JS'])
# print(prog['Python'][1])
# print(prog['Java']['JSE'])
# print(prog['Name']['name1']['subname1']['Ankana'][2])


# employees = {
#     "emp1": {"name": "Alice", "age": 30},
#     "emp2": {"name": "Bob", "age": 25}
# }
# print(employees['emp1']['name'])
    
    
# #Dictionary comprehensions
# squares = {}
# for i in range(1,6):
#     squares[i] = i*i
# print(squares)   

# squares = {x: x*x for x in range(1,6)}
# print(squares)     

# cubes = {x: x*x*x for x in range(1,6)}
# print(cubes)    

# even_numbers = {}
# for i, key in enumerate(range(2, 10, 2)):
#         even_numbers[i+1] = key
# print(even_numbers)  

# even = {}
# for i, x in enumerate(range(2, 6, 2)):
#     even[f'Even {i+1}'] = x 
# print(even)        
             
             
# #Example 2
# data1 = {1 : "Ball", 2: "Bat", 4 : "Gloves", 6 : "Cap"}
# data1[3] = "Wicket"
# print(data1)  
# all_data = list(data1.keys())
# all_data.sort()
# print(all_data)          

# for key in sorted(data1.keys(), reverse=True):
#     print(f" {key} : {data1[key]}")             
    
# '''
# sort () is a method to sort a list, original list is changed
# sorted is a function in any iterable object, original list is unchanged

# '''    

# #setdefault() method
# data2 = {1 : "Ball", 2: "Bat", 4 : "Gloves", 6 : "Cap"}
# data2.setdefault(5, "Helmet")
# print(data2)    

# for key in sorted(data2.keys(), reverse=False):
#     print(f" {key} : {data2[key]}")


# #Example 3
# words = ["banana", "apple", "kiwi"]   
# update_data = sorted(words, key=len, reverse=True)
# print(update_data)    
    

# #Using defaultdict from collections
# from collections import defaultdict

# dd = defaultdict(int)
# dd["a"] += 1
# print(dd)    


# #Using counter for counting
# from collections import Counter

# words = ["apple", "mango", "cherry", "mango", "banana", "cherry", "kiwi", "cherry", "kiwi"]
# count = Counter(words)
# print(count)

# #Grouping people by department
# employees = [
#     {"name": "Amit", "dept": "HR"},
#     {"name": "Sara", "dept": "IT"},
#     {"name": "Raj", "dept": "IT"},
#     {"name": "Anna", "dept": "HR"}
# ]

# from collections import defaultdict
# grouped = defaultdict(list)

# for emp in employees:
#     grouped[emp["dept"]].append(emp["name"])

# print(grouped)    


# #Modify dictionary
# data2 = {1 : "Ball", 2: "Bat", 4 : "Gloves", 6 : "Cap"}
# data2[1] = "Green Ball"
# print(data2)

# #len() in dictionary
# data = {1 : "Ball", 2: "Bat", 4 : "Gloves", 6 : "Cap"}
# print(len(data))

#More examples:
person = {
    "name": "Ankana",
    "age": 28,
    "city": "Kolkata"
}

for key, value in person.items():
    print(f"{key} : {value}")

data={}
data['items'] = [('a', 1), ('b', 2), ('c', 3)]
print(data)
for key, value in data['items']:
    print(f"{key} : {value}")


#List of dictionary
students = [
    {"name": "Anu", "math": 90, "science": 88},
    {"name": "Ravi", "math": 78, "science": 75},
    {"name": "Meera", "math": 85, "science": 80}
]

for student in students:
    print(f"{student["name"]} - Math: {student["math"]}, Science: {student['science']}")

#Nested dictionary
weather_data = {
    "Kolkata": {"temperature": 35, "humidity": 80},
    "Delhi": {"temperature": 40, "humidity": 20},
    "Mumbai": {"temperature": 30, "humidity": 90}
}

for key, value in weather_data.items():
    print(f"{key} -> temp : {value["temperature"]}")

inventory = [
    {
        "product": "Laptop",
        "details": {"brand": "HP", "price": 55000, "stock": 10}
    },
    {
        "product": "Mobile",
        "details": {"brand": "Samsung", "price": 15000, "stock": 25}
    }
]

for item in inventory:
    product = item["product"]
    details = item["details"]
    print(f"{product} - Brand: {details["brand"]} - Price{details["price"]} - Stock{details["stock"]}")


hotel = {
    "Hotel Taj": {"rooms": ["Deluxe", "Suite", "Economy"], "rating": 4.8},
    "Hotel Sun": {"rooms": ["Economy", "Standard"], "rating": 4.2}
}

for hotel_name, info in hotel.items():
    print(f"{hotel_name} - Rating {info["rating"]}")
    print(f"Available rooms : {info["rooms"]}")


company = {
    "HR": [
        {"name": "Rita", "age": 30},
        {"name": "Manoj", "age": 35}
    ],
    "IT": [
        {"name": "Sita", "age": 28},
        {"name": "Aman", "age": 26}
    ]
}

for dept, employees in company.items():
    print(f"\nDepartment : {dept}")
    for emp in employees:
        print(f"Emplyee name: {emp["name"]}, Age: {emp["age"]}")