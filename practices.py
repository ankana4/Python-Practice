
class Solution:
    def factorial (self, n):
        result = 1
        for i in range(1, n+1):
            result = result * i
        return result
    
obj = Solution()    
data = obj.factorial(n = 4)
print(data)     

class Solution:
    def sumOfSquares(self, number):
        sum = 0
        for i in range(1, number+1):
            sum = sum + i*i
        return sum

obj = Solution()
data = obj.sumOfSquares(3)
print(data)        


#reverse of a number and palindrome
def reverse(n):
    rev = 0
    temp = n
    while n > 0:
        last_digit = n % 10
        rev = rev * 10 + last_digit
        n = n // 10
    if rev == temp:
        return True
    else:
        return False

reve = reverse(n = 5855)
print(reve)
           

           