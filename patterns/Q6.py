'''
12345
1234
123
12
1
'''
n = 5
for i in range(n, 0, -1):
    for j in range(1, i+1):
        print(j, end="")
    print()    
    
#Another approach
num = 1
for i in range(0, n):
    num = 1
    for j in range(n, i, -1):
        print(num, end="")
        num += 1
    print()        