class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)) # to remove all the non-alphanumeric characters from the string
        s = s.lower()
        for i in range(0, len(s)//2):
            if s[i] == s[len(s)-i-1]:
                continue
            else:
                return False
        return True
