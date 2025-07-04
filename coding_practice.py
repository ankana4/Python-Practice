n = 5
fact = 1
for i in range(1, n+1):
    fact = fact*i
print(fact)    
    
    
s = 'mom'
temp = ''
for i in s[::-1]:
    temp = temp + i
print(temp)  
print(s)  
if temp == s:
    print("Palindrome")
else:
    print("Not")        
    
    
def reverse_data(str_data):
    temp = ''
    for i in range(len(str_data), 0, -1):
        temp = temp+str_data[i-1]
    return temp    
        
data = reverse_data(str_data="ognaM")    
print(data)        


a = 'listen'
b = 'silent'

if len(a) != len(b):
    print("Not anagram")
else:  
    is_anagram = True  
    for ch in a:
        if a.count(ch) != b.count(ch):
            print("Not anagram")
            is_anagram = False
            break
    if is_anagram:
        print("A")
    else:
        print("N")      

list1 = [3, 5, 2, 4, 1]
target = 2
for i in range(0, len(list1)):
    if i in list1 and list1[i] == target:
        # if list1[i] == target:
            print(i)
    else:
        print(-1)                
idx = -1
for i in range(0, len(list1)):
    if target == list1[i]:
        idx=i    
        break
print(idx)         
            
idx = -1                
for idx1, val in enumerate(list1):
    if target == val:
        idx = idx1    
        break
print(idx)    
               

def majority_element_subarray(arr, queries):
    def majority_element(start, end):
        count = {}
        for num in arr[start:end+1]:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for num, freq in count.items():
            if freq > (end - start + 1) / 2:
                return num
        return -1

    result = []
    for start, end in queries:
        result.append(majority_element(start, end))
    return result               
arr = [1, 1, 2, 2, 1, 1]
queries = [(0, 5), (0, 3), (2, 3)]

result = majority_element_subarray(arr, queries)
print(result)
