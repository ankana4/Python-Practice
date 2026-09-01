#Print Name N times using Recursion


#Problem Description: Given an integer N, write a program to print your name N times.

def print_name(i, n):
    if i > n:
        return
    print("Treehouse")
    print_name(i+1, n)

n = 2
print_name(1, n)    