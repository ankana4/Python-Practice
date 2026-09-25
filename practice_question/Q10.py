#Orders by customer
orders = [
    {"customer": "A", "amount": 100},
    {"customer": "B", "amount": 200},
    {"customer": "A", "amount": 300},
    {"customer": "C", "amount": 150},
    {"customer": "B", "amount": 100}
]

order_dict = {}

for order in orders:
    cus = order["customer"]
    amt = order["amount"]
    
    if cus not in order_dict:
        order_dict[cus] = {
            "orders": 0,
            "total": 0
        }
    order_dict[cus]["orders"] += 1
    order_dict[cus]["total"] += amt
print(order_dict)        
        