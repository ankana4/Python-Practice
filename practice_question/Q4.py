#Group students by age
students = [
    {"name": "A", "age": 20},
    {"name": "B", "age": 21},
    {"name": "C", "age": 20},
    {"name": "D", "age": 22},
    {"name": "E", "age": 21}
]
temp_dict = {}
for stud in students:
    age = stud["age"]
    if age not in temp_dict:
        temp_dict[age]= []
    temp_dict[age].append(stud)
print(temp_dict)         
    

#Group only names by age
temp_dict={}
for stud in students:
    age = stud["age"]
    name=stud["name"]
    if age not in temp_dict:
        temp_dict[age]=[]
    temp_dict[age].append(name)
print(temp_dict)            


#Count students by age
count_by_age={}
for stud in students:
    age=stud["age"]
    if age not in count_by_age:
        count_by_age[age]=1
    count_by_age[age]+=1
print(count_by_age)        