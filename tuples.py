'''
Tuple is an immutable ordered elements in python
'''

#Creating a tuple
t1 = (1,2,3)
print(t1)

#Tuple with 1 item, need coma
t2 = (1,)
print(t2)

#Tuple without parantheses
t3 = 4,5,6
print(t3)

#Mixed data types
t4 = ("apple", 4, 5,6 )
print(t4)

#Accessing tuple elements
t5 = (10, 20, 30, 40)
print(t5[0])
print(t5[1])
print(t5[2])
print(t5[-1])
print(t5[0:2])

#Looping through a tuple
t6 = ('apple', "banana", 'cherry')

for item in t6:
    print(item)

#Tuple unpacking
person = ("Alice", 25, "Engineer")
name, age, job = person
print(name)
print(age)
print(job)

#Taking user input
list = []
for data in range(2):
    name = input("Enter a name : ")
    age = input("Enter age : ")
    list.append((name, age))
print(list)    

#Returning multiple values from functions
def get_user_info():
    return("Alice", 20, "HR")

name, age, job=get_user_info()
print(name, age, job)


#As dictionary keys
location_weather = {
    ("Kolkata", "2024-06-09") : "Rainy",
    ("Delhi", "2024-06-09"): "Sunny"
}

print(location_weather[("Kolkata", "2024-06-09")])

#Used with sets
coordinates = {(1,2), (3,4), (5,6)}
print((3,4) in coordinates)   #tuples are hashable means items in tuple immutable, caanot modified

#Create a tuple with your name age and city
#Unpack it into variables
for item in range(1,3):
    name = input("Enter name: ")
    age = input("Enter age: ")
    city = input("Enter city: ")
    person = name, age, city
    # print(person)    

    name, age, city = person
    print(name)
    print(age)
    print(city)

#Store a list of location coordinates as tuples
list = []
for i in range(2):
    coordinates1 = input("Enter first location coordinate: ")
    coordinates2 = input("Enter second location coordinate: ")
    list.append((coordinates1, coordinates2))
print(list)    


#Use tuples as dictionary keys for mapping date to temperature.
dict_obj = {}
for i in range(2):
    date = input("Enter date range: ")
    location = input("Enter location: ")
    temparature = input("Enter temaprature: ")
    key = (date, location)
    dict_obj[key] = temparature
print(dict_obj) 

for k, v in dict_obj.items():
    print(f"{k} : {v}")   
    