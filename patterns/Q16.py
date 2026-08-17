'''
A
B B
C C C
D D D D
E E E E E

'''
n = 5
for i in range(0, n):
    for j in range(0, i+1):
        print(chr(65+i), end=" ")
    print()    
