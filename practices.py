
# class Solution:
#     def factorial (self, n):
#         result = 1
#         for i in range(1, n+1):
#             result = result * i
#         # return result
    
# obj = Solution()    
# data = obj.factorial(n = 4)
# print(data)     

# class Solution:
#     def sumOfSquares(self, number):
#         sum = 0
#         for i in range(1, number+1):
#             sum = sum + i*i
#         return sum

# obj = Solution()
# data = obj.sumOfSquares(3)
# print(data)        


# #reverse of a number and palindrome
# def reverse(n):
#     rev = 0
#     temp = n
#     while n > 0:
#         last_digit = n % 10
#         rev = rev * 10 + last_digit
#         n = n // 10
#     if rev == temp:
#         return True
#     else:
#         return False

# reve = reverse(n = 5855)
# print(reve)



# #Armstrong
# def isAramstrong(n):
#     rev = 0
#     temp = n
#     while (n > 0):
#         last_digit = n % 10
#         rev = rev + last_digit*last_digit*last_digit
#         n = n //10
#     if rev == temp:
#         return True
#     else:
#         return False

# data = isAramstrong(100)
# print(data)                   


# #GCD of two number or HCF of two number
# def factor(n):
#     factors = []
#     for i in range(1, n+1):
#         if n % i == 0:
#             factors.append(i)
#     return factors
# a = int(input("Enter value for a: "))
# b = int(input("Enter value for b: "))
# factor_of_a = factor(a)
# factor_of_b = factor(b)

# result = 0
# for i in factor_of_a:
#     if i in factor_of_b:
#         if i > result:
#             result = i  
# print(result)                  
      
# #Optimize approach
# def gcd(a, b) -> int:
#     for i in range(min(a,b), 0, -1):
#         if a % i == 0 and b % i == 0:
#             return i 
#     return 1    
# print(gcd(12, 8))      

# #gfg optimize approach
# def gcd(a, b):
#     while(b != 0):
#         temp = b
#         b = a%b
#         a = temp
#     return a    

# print(gcd(3, 6))      
                 
# #Prime numbers
# def isPrime(n):
#     factors = []
#     for i in range(1, n+1):
#         if n % i == 0:
#             factors.append(i)
#     if len(factors) == 2:
#         return True
#     else:
#         return False
     
# print(isPrime(3))                   

# #optimize approach1
# def isPrime(n):
#     no_of_factors=0
#     for i in range(1, n+1):
#         if n % i == 0:
#             no_of_factors += 1
#     return no_of_factors == 2
     
# print(isPrime(7))   

# #optimize approach2 
# def isPrime(n):
#     if n == 1:
#         return False
#     for i in range(2, n):
#         if n%i == 0 :
#             return False
#     return True
# print(isPrime(1))        

# # Optimize approach3

# '''
# You are given a string s containing only lowercase letters. You need to count the number of vowels and the number of consonants.
# '''
# s = input("Enter a string value: ")
# vc=0
# cc=0
# for i in s:
#     if i == " ":
#         continue
#     if i not in ['a', 'e', 'i', 'o', 'u']:
#         cc += 1
#     else:
#         vc += 1
# if vc > cc:
#     print("Yes", vc, cc)
# elif vc < cc:
#     print("No")
# else:
#     print("Same")                    


'''
Given a string S. Count the characters that have ‘N’ number of occurrences. If a character appears consecutively it is counted as 1 occurrence.
'''

# s = 'geekforgeeks'
s = "geeksforgeeks"
N = 2
no_of_occurence = {}
i = 0
j = 0
c = 0
while(j<len(s)): #5<6
    if s[i] == s[j]: 
        j += 1 # j = 5(t)
    else:
        no_of_occurence[s[i]] = no_of_occurence.get(s[i], 0)+1
        i = j  #i = 5(t)
no_of_occurence[s[i]] = no_of_occurence.get(s[i], 0)+1  
for key, val in no_of_occurence.items():
    if val == N:
        c += 1                
print(c)    
            
    