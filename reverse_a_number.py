def reverse_a_number(num:int)->int:
    rev = 0
    while(num > 0):
        lastDigit = num % 10
        rev = rev * 10 + lastDigit
        num = num // 10
        
    return rev    
        

def solve():
    num = int(input("Enter a number: "))
    if num < 0:
        num = num * -1
        rev = reverse_a_number(num) * -1
    else:
        rev = reverse_a_number(num)
    
    print(rev) 
solve()  