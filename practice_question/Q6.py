#Calculate total salary by department
employees = [
    {"name": "A", "department": "IT", "salary": 50000},
    {"name": "B", "department": "HR", "salary": 40000},
    {"name": "C", "department": "IT", "salary": 60000},
    {"name": "D", "department": "HR", "salary": 45000}
]
emp_dict = {}
for emp in employees:
    dept = emp["department"]
    sal = emp["salary"]
    if dept not in emp_dict:
        emp_dict[dept] = sal
    else:    
        emp_dict[dept]+=sal
print(emp_dict)        