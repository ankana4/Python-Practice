#Print all Divisors of a given Number
N=36
new_list=[]
for i in range(1, N+1):
    if N%i==0:
        new_list.append(i)
print(new_list)        
