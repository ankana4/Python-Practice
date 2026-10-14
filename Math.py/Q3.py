#Find gcd and lcm with more optimized approach
a = int(input("Enter a: "))
b = int(input("Enter b: "))
x = a
y = b
while b!=0:
    a,b=b, a%b
gcd=a
lcm = (x*y)//gcd
print("Gcd and lcm is ", gcd," ",lcm)     