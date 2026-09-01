#Print 1 to N using Recursion


#Problem Description: Given an integer N, write a program to print numbers from 1 to N.

def print_num(i, n):
    if i>n:
        return
    print(i)
    print_num(i+1, n)

n= int(input("Enter a  number: "))
print_num(1, n)   