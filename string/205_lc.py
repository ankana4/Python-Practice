#205. Isomorphic Strings
def ispomorphicStr(s, t):
    s_dict={}
    t_dict={}
    for i in range(len(s)):
        if s[i] in s_dict and s_dict[s[i]]!=t[i]:
            return False
        if t[i] in t_dict and t_dict[t[i]]!=s[i]:
            return False
        
        s_dict[s[i]]=t[i]
        t_dict[t[i]]=s[i]
    
    return True

s="egg"
t="add"
print(ispomorphicStr(s, t))
       