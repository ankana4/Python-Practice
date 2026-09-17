#Print all Divisors of a given Number
N=36
new_list=[]
for i in range(1, N+1):
    if N%i==0:
        new_list.append(i)
print(new_list)        

#Another approach
res = []
i = 1
while i*i <= N:
    if N%i == 0:
        res.append(i)
        if N//i != i:
            res.append(N//i)
    i+=1        
print(sorted(res))               