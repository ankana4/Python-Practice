# Check if a number is prime or not
n = 6
c = 0
for i in range(1, n+1):
    if n%i == 0:
        c+=1
if c == 2:
    print("Prime number")
else:
    print("Not prime number")            
 
#Another approach
while i*i <= n:
    if n%i == 0:
        c+=1
        if n//2 % i != i:
            c+=1
if c == 2:
    print("Prime")
else:
    print("Not Prime")                
        
#Another approach

def isPrime(n):
    if n <= 1:
        print("False")

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            print("False")

    print("True")       
    
ob = isPrime(6)  
print(ob)  