'''
The Conditional Statements 
- if -> It select the statement block to execute based on the result of one or more expressions.

'''
#if statement
x = 10
if x > 5:
    print("X is greater than 5")

#if...else statement    
x = 3
if x > 5:
    print("X is greater tnan 5")
else:
    print("X is less than 5")        

#if...elif...else statement
result = 2
if (result == 1):
    print("Got 1")
elif (result == 2):
    print("Pass")
else:
    print("Failed") 
    
#nested conditions
x = 10
if x > 0:
    if x % 2 == 0:
        print("X is positive odd number") 
    else:
        print("X is even number")       
       
#logical operators
age = 25
has_id = True

if age >= 25 and has_id:
    print("Authorized")        


'''
Industry Level Examples 

'''

#Order discount logic
order_total = 500
is_member = True

if order_total >= 750 and is_member:
    print("Block 1 execute")
    discount = 0.20
    
elif order_total > 500 and not is_member:
    print("Block 2 execute")
    discount = 0.10
    
elif order_total > 300:
    print("Block 3 execute")
    discount = 0.05

else:
    discount = 0
    
final_price = order_total * (1 - discount) 
print(f"Final price is {final_price}")    


# Example 2
user_role = 'admin'
is_active = True

if is_active:
    if user_role == 'admin':
        print("Access granted to admin")
    elif user_role == "contructor":
        print("Access granted to contructor")
        
    else:
        print("Limited access")

else:
    print("Account inactive, access denied")            


#Example 3
email = "abc@gmail.com"
password = "1Secure@123"

if '@' in email and len(password) >= 8:
    print("Valid credentials")
    
else:
    print("Wrong email or password too short")    