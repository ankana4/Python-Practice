#Given a number x, print the numbers from x to 0 in decreasing order in a single line.
x=int(input())
list_data=[]
while(x>=0):
    list_data.append(x)
    x-=1
print(*list_data)    
    