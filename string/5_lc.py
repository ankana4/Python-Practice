#5. Longest Palindromic Substring

#Brute-force approach-1
def longestPalindrom(s):
    n=len(s)
    longest=""
    for i in range(n):
        for j in range(i, n):
            substring=s[i:j+1]
            if substring == substring[::-1]:
                if len(substring)>len(longest):
                    longest=substring
    return longest


s='babad'
print(longestPalindrom(s))                

#Without slicing
def isPalindrome(s, left, right):
    while left<right:
        if s[left]!=s[right]:
            return False
        right-=1
        left+=1
    return True

def longestPalindrome(s):
    n=len(s)
    longest=''
    
    for i in range(n):
        for j in range(n):
            if isPalindrome(s, i, j):
                if j-i+1>len(longest):
                    longest=s[i:j+1] 
    return longest

s='bababad'
print(longestPalindrome(s))                   

#Expand around center approach
def expand(s, left, right):
    while left>=0 and s[right]<len(s) and s[left]==s[right]:
        left-=1
        right+=1
        
    return s[left+1:right]

def longestPalindrome(s):
    n=len(s)
    longest=""
    for i in range(n):
        odd=expand(s, i, i)
        even=expand(s, i, i+1)
        if len(odd)>len(longest):
            longest=odd
        if len(even)>len(longest):
            longest=even
    return longest

s='babad'
print(longestPalindrom(s))                