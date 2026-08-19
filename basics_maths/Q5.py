#Check if a number is Armstrong Number or not
def is_armstrong(n):
    k = len(str(n))
    original = n
    sum = 0
    while n>0:
        ld=n%10
        sum+=ld**k
        n=n//10
    return sum==original

n = 1532
if is_armstrong(n):
    print("Armstrong")
else:
    print("Not Armstrong")
