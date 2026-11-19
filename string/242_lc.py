#242. Valid Anagram

#Brute-force approach
def isAnagaram(s, t):
    if len(s)!=len(t):
        return False
    return sorted(s)==sorted(t)

s="anagram"
t="nagaram"
print(isAnagaram(s, t))