'''
Given two integer variables x and y, perform the following operations:

p: Addition of x and y
q: Subtraction of y from x
r: Multiplication of x and y
s: Floating-point division of x by y
t: Integer division of x by y
'''

def arithmetic_op(x, y):
    p = x+y
    q = x-y
    r=x*y
    s=x/y
    t=x//y
    u=x%y
    return (p, q, r, f"{s:.3f}", t, u)

ao = arithmetic_op(7, 6)
print(ao)