'''
E
D E
C D E
B C D E
A B C D E

'''
n = 6
ch = 'F'
for i in range(1, n):
    for j in range(i, 0, -1):
        print(chr(ord(ch)-j), end=" ")
    print()