'''
Assignements for conditional statements
'''

# Check postive, negative and zero
num =   float(input("Enter a number: "))

if num > 0:
    print("Number is positive.")
elif num < 0:
    print("Number is negative.")
    
else:
    print("Number is zero")        
    
   

# Odd or even
num = float(input("Enter a number: "))

if num % 2 == 0:
    print("Number is even")

else:
    print("Number is odd")       


#Find largest of three numbers
x = int(input("Enter a number"))
y = int(input("Enter a number"))
z = int(input("Enter a number"))

if x >= y and x >= z:
    print("X is the largest number")
    
elif y >=  z and y >= x:
    print("Y is the largest number")
    
else:
    print("Z is the largest number ")
            

# Grade Checker

x = int(input("Enetr a number : "))

if x >= 90 and x <= 100:
    print("Grade is A") 
elif x >=80 and x <= 89:
    print("Grade is B")
elif x >=70 and x <=79:
    print("Grade is C")
elif x >=60 and x<=69:
    print("Grade is D")
    
else:
    print("Grade is F")                


# Leap year checker

x = int(input("Enter a year : "))

if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
    print(f"the year {x} is leap year")
    
else:
    print(f"{x} is not a leap year")    

# Traffic light logic

x = input("Enter a traffic signal : ").lower()
if x == "red":
    print("Stop")
elif x == "yellow":
    print("Wait")
elif x == "green":
    print("Go") 
else:
    print("Invalid input")       
        
# Login validation
username="ankana"
password="1234@"

name = input("Enter username : ")
passkey = input("Enter password : ")

if name == username and passkey == password:
    print("Matched")
else:
    print("Invalid")            


#Movie ticket price
age = int(input("Enter age : "))  #-10

if age > 0 and age < 5:
    price = 0
elif age >= 5 and age <= 12:
    price = 100
elif age >= 13 and age <= 60:
    price = 150
elif age > 60:
    price = 80
else:
    price = -1
    print(f"Invalid age")  
    
print(f"Price is {price}")      


# Number divisibility
x = float(input("Enter a number : "))

if x >= 90 and x <= 100:     # x = 65
    print("A")
elif x >= 80 and x <= 89:
    print("B")
elif x >= 70 and x <= 79:
    print("C")
elif x >= 60 and x <= 69:
    print("D")
elif x >= 0 and x <= 59:
    print("F")
else:
    print("Invalid grade")             
             



#Ecommerce discount logic

cart_value = float(input("Enter total cart value: "))

if cart_value >= 5000:
    discount = 0.25

elif cart_value >= 2000 and cart_value <= 5000:
    discount = 0.10
    
elif cart_value >= 0 and cart_value < 2000:
    discount = 0

else:
    discount = 0
    print("Cart value should not take negative")

discounted_value = cart_value * discount
final_price = cart_value - discounted_value
print(f"discounted value is {discounted_value}")
print(f"final price is {final_price}")


#Electricity bill estimator

unit = float(input("Enter unit value: "))
if unit >= 0 and unit < 100:
    rate = 2
elif unit >=100 and unit <= 300:
    rate = 5
elif unit > 300:
    rate = 8    
else:
    rate = 0
    print("Invalid unit value")    
final_price = unit * rate
print(f"Final price is {final_price}")    
    
    
#ATM withdrawal condition
current_balance = int(input("Enter current balance : ")) 
amount_withdraw = int(input("Enter amount to withdraw: ")) 
daily_limit = 20_000

if current_balance >= 0 and amount_withdraw > 0:
    if amount_withdraw <= current_balance and amount_withdraw <= daily_limit:
        print("success") 
    elif amount_withdraw > current_balance and amount_withdraw > daily_limit:
        print(f"Withdrawl amount is greater than {current_balance} and {daily_limit}")
    elif amount_withdraw > current_balance:
        print(f"you cannot withdraw because current balance is {current_balance}")          
    elif amount_withdraw > daily_limit:
        print(f"You exceed daily limit transaction because current balance is {current_balance}")          
else:
    print("Invalid input")        

# Loan eligibility 
salary = float(input("Enter salary amount: "))
years_of_employement = float(input("Enter years of employment: ")) 
credit_score = float(input("Enter credit score : ")) 

if salary > 0 and years_of_employement > 0 and credit_score > 0: 
    if salary > 30_000 and years_of_employement > 2 and credit_score > 700:
        print("eligible")
    else:
        print("Not eligible")    
else:
    print("Invalid input")


'''
You are tasked with writing a function that simulates the battery management system of a robot. 
The function takes two inputs: an integer battery representing the battery percentage (ranging from 0 to 100), 
and a boolean is_charging indicating whether the robot is currently charging (True or False). 
Based on these inputs, the function should return a string describing the robot’s current status. 
If the battery level is 80 or above and the robot is charging, it should return "Battery full, stop charging"; 
if not charging, return "Ready for heavy tasks". If the battery is between 30 and 79 (inclusive), 
and the robot is charging, return "Charging, avoid heavy tasks"; otherwise, return "Perform light tasks". 
If the battery is below 30 and charging, return "Low battery, continue charging"; 
if not charging, return "Critical! Return to charging dock". If the battery value is not within 0 to 100, return "Invalid battery level". 
The function must handle all these conditions accurately using conditional statements. 
'''

def battery_management(battery : int, is_charging : bool)-> str:
    if battery >= 0 and battery <= 100:  
        if is_charging:
            if battery >= 80:
                return "Full"
            elif battery >= 30 and battery <= 79:
                return "Charging"
            elif battery < 30:
                return "Low battery"
        else:
            if battery >= 80:
                return "ready for heavy tasks"
            elif battery >=30 and battery <= 79:
                return "perform light tasks"
            elif battery < 30:
                return "Critical"     
    else:
        return "Invalid battery level"  
    
battery = int(input("Enter battery level: "))
is_charging = input("Enter value: ") == 'true'
result = battery_management(battery=battery, is_charging=is_charging)
print(f"Result is {result}")
              