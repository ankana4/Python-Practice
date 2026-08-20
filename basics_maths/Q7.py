#Check if a number is prime or not
n = 5
c = 0
for i in range(1, n+1):
    if n%i == 0:
        c+=1
if c == 2:
    print("Prime number")
else:
    print("Not prime number")            