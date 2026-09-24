#Find maximum salary employee
employees = [
    {"name": "A", "salary": 50000},
    {"name": "B", "salary": 75000},
    {"name": "C", "salary": 60000}
]
emp_dict={}
max_salary = 0
for emp in employees:
    name=emp["name"]
    sal = emp["salary"]
    if sal > max_salary:
        max_salary = sal
        max_name = name
emp_dict[max_name]=max_salary
print(emp_dict)            