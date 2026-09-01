#Print N to 1 using Recursion

#Problem Description: Given an integer N, write a program to print numbers from N to 1.

def print_num(i, n):
    if i<n:
        return
    print(i)
    print_num(i-1, n)

n = int(input("Enter a number: "))
print_num(n, 1)    