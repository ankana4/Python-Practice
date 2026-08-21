#Find GCD of two numbers
def find_gcd(a, b):
    gcd = 1
    for i in range(1, min(a, b)+1):
        if a%i == 0 and b%i == 0:
            gcd = i
    return gcd

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number "))

print(find_gcd(num1, num2))        

#Optimize approach
def find_gcd_of_number(n1, n2):
    for i in range(min(n1, n2), 0, -1):
        if n1%i == 0 and n2%i == 0:
            return i
    return 1

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number "))

print(find_gcd_of_number(num1, num2))