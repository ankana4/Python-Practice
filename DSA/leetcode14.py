   
a = ['flower', 'flow', 'fly']
list1 = ['Abc', 'abcde', 'abrt', 'ab', 'abc'] 

a1 = [i.lower() for i in list1]    
temp = ''
str_data = ''
    
for j in range(0, min(len(a[0]), len(a[1]))):  
    if a[0][j] == a[1][j]:
        temp += a[0][j]
    else:
        break
# print(temp)
        
for i in range (2, len(a)):
    word = a[i]
    str_data = ''
    for k in range (min(len(temp), len(word))):  #temp='abc'
        if temp[k] == word[k]: 
            str_data += temp[k]
    if len(str_data) < len(temp):
        temp = str_data
print(temp)                        
    
    
a = ['flower', 'flow', 'fly']
p = sorted(a)   
print(p)          

word1 = p[0]
word2 =  p[-1]
temp = ''

for i in range(min(len(word1), len(word2))):
    if word1[i] == word2[i]:
        temp += word1[i]
    else:
        break 
print(temp)       
           