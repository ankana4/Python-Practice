
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