#242. Valid Anagram

#Brute-force approach
def isAnagaram(s, t):
    if len(s)!=len(t):
        return False
    return sorted(s)==sorted(t)

s="anagram"
t="nagaram"
print(isAnagaram(s, t))


#Optimal Approach
def isAnagram(s, t):
    if len(s)!=len(t):
        return False
    freq={}
    
    for ch in s:
        freq[ch]=freq.get(ch, 0)+1
    for ch in t:
        if ch not in freq:
            return False
        freq[ch]-=1
        
        if freq[ch]<0:
            return False
    return True

s="aab"
t="aba"
print(isAnagaram(s, t))         