'''
     A     
    A B A
   A B C B A
  A B C D C B A
 
'''
n = 5
for i in range(0, n):
    for j in range(0, n-i-1):
        print(" ", end="")
    #Character
    ch = 'A'
    breakpoint = (2*i+1) // 2
    for j in range(0, 2*i+1):
        print(ch, end="")
        if j < breakpoint:
            ch = chr(ord(ch)+1)
        else:
            ch = chr(ord(ch)-1)
    for j in range(0, n-i-1):
        print(" ", end="")
    print()                
