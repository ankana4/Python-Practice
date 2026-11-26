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
# print(longestPalindrom(s))                

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