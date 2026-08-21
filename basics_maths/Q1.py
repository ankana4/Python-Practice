#Count of digits in a number
import math

numbers = 32145
c=0
while numbers>0:
    c+=1
    numbers=numbers//10
print(c)

#Alternate approach
def CountDigits(numberts):
    cnt = int(math.log10(numbers)+1)
    
    return cnt

if "__main__" == __name__:
    numbers = 32145
    print(CountDigits(numbers))
    