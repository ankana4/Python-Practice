'''
Given a mathematical equation that contains only numbers and +, -, *, /. 
Print the equation in reverse, such that the equation is reversed, but the numbers remain the same.
It is guaranteed that the given equation is valid, and there are no leading zeros.
'''
s = "20-3+5*2"
result=""
num=""

for ch in s:
    if ch.isdigit():
        num+=ch
    else:
        result=ch+num+result
        num=""
result=num+result
print(result)            