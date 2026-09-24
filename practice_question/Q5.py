#Group employees by department
employees = [
    {"name": "Amit", "department": "IT"},
    {"name": "Rahul", "department": "HR"},
    {"name": "Priya", "department": "IT"},
    {"name": "Neha", "department": "Finance"},
    {"name": "Rohan", "department": "HR"}
]

emp_dict={}
for emp in employees:
    dept = emp["department"]
    name=emp["name"]
    if dept not in emp_dict:
        emp_dict[dept] = []
    emp_dict[dept].append(name)
print(emp_dict)        