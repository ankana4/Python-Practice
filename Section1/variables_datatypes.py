# print("Welcome to BMI calculator")

# weight = float(input("Enter your weight (in kg): "))
# height = float(input("Enter your height (in meters): "))

# bmi_calculator = weight / height**2

# print(f"Your BMI is {bmi_calculator}")

# if bmi_calculator < 18.5:
#     print("You are in under weight")

# elif 18.5 <= bmi_calculator < 24.9:
#     print("You are in normal weight")

# elif 24.9 <= bmi_calculator < 29.9:
#     print("You are in over weight")

# else:
#     print("Your are obese")        
        
        
   
   
print("Welcome")
a = float(input("Enter first number : "))
b = float(input("Enter second number: "))

digit = str(input("Enter your choice : "))

if digit == '+':
    print(f"Sum is {a+b}")
elif digit == '-':
    print("Sub is ",abs(a-b)) 
elif digit == "/":
    print("Div is ", a/b)
elif digit == '*':
    print(f"Mul is {a*b}")  

else:
    print("Give wrong input!")                    