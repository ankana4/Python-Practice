s = "()[]{}"

lst = []
for i in range(0, len(s)):
    currChar = s[i]
    if currChar == '(' or currChar == '{' or currChar == '[':
        lst.append(currChar)
        
    else:
        if len(lst) == 0:
            print("False")
            
        if currChar == ')' and lst[-1] != '(':
            print("False")    
        
        elif currChar == '}' and lst[-1] != '{':
            print("False")    
        
        elif currChar == ']' and lst[-1] != '[':
            print("False")  
        
        lst.pop()        
if len(lst) != 0:
    print("False")
else:
    print("True")                          