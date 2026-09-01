#Factorial of a Number : Iterative and Recursive

#Problem Statement: Given a number X,  print its factorial.

def fact_of_n(n):
    if n == 0:
        return 1
    return n * fact_of_n(n-1)

n = int(input("Enter a number: "))
print(fact_of_n(n))