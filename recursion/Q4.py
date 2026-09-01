#Sum of first N Natural Numbers

#Problem Statement: Given a number ‘N’, find out the sum of the first N natural numbers .

def sum_of_naturals(n):
    if n == 0:
        return 0
    return n + sum_of_naturals(n-1)

n = int(input("Enter a number: "))
print(sum_of_naturals(n))