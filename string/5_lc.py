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