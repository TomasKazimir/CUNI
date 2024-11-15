def palindrome_1(s):
    n = len(s)
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            return False
    return True


def palindrome_2(s):
    if len(s) <=1 :
        return True
    else:
        return s[0] == s[-1] and palindrome_2(s[1:-1])

word1 = "abbabcbabba"
print(palindrome_1(word1))
print(palindrome_2(word1))

word2 = "abcdefgh"
print(palindrome_1(word2))
print(palindrome_2(word2))