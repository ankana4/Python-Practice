#Given an integer n, return all the divisors of n in the ascending order.
n =21191
list_data=[]
for i in range(1, n+1):
    if n%i == 0:
        list_data.append(i)
print(*list_data)        
        