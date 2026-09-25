#Group products by category
products = [
    {"name": "Laptop", "category": "Electronics", "price": 70000},
    {"name": "Phone", "category": "Electronics", "price": 30000},
    {"name": "Chair", "category": "Furniture", "price": 5000},
    {"name": "Table", "category": "Furniture", "price": 10000}
]

prod_dict={}
for prod in products:
    category = prod["category"]
    name = prod["name"]
    
    if category not in prod_dict:
        prod_dict[category] = []
    prod_dict[category].append(name) 
print(prod_dict)     

#total price by category
prod_dict = {}
for prod in products:
    category = prod["category"]
    price = prod["price"]
    if category not in prod_dict:
        prod_dict[category] = price
    else:
        prod_dict[category]+= price
print(prod_dict)            
  