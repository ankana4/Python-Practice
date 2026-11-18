#1614. Maximum Nesting Depth of the Parentheses

def maxDepth(s:str)->int:
    count=0
    max_depth=0
    
    for ch in s:
        if ch=='(':
            count+=1
            max_depth=max(max_depth, count)
        elif ch==')':
            count-=1
    return max_depth

s="(1+(2*3)+((8)/4))+1"
print(maxDepth(s))            