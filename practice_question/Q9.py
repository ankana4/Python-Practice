#Create nested grouping
employees = [
    {"name": "A", "department": "IT", "city": "Kolkata"},
    {"name": "B", "department": "IT", "city": "Delhi"},
    {"name": "C", "department": "HR", "city": "Kolkata"},
    {"name": "D", "department": "IT", "city": "Kolkata"}
]

emp_dict = {}
for emp in employees:
    dept = emp["department"]
    name = emp["name"]
    city = emp["city"]
    
    if dept not in emp_dict:
        emp_dict[dept] = {}
    
    if city not in emp_dict[dept]:
        emp_dict[dept][city] = []
    emp_dict[dept][city].append(name)
print(emp_dict)            
   