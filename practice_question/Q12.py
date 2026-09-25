#Find most frequent age
users = [
    {"name": "A", "age": 20},
    {"name": "B", "age": 25},
    {"name": "C", "age": 20},
    {"name": "D", "age": 30},
    {"name": "E", "age": 20},
    {"name": "F", "age": 25}
]
user_dict={}

for u in users:
    age = u["age"]
    if age in user_dict:
        user_dict[age] += 1
    else:
        user_dict[age] = 1
max_c=0
max_a=None
for k, v in user_dict.items():
    if v>max_c:
        max_c=v
        max_a=k
print(max_a)                    